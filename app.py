from flask import Flask , render_template, request, jsonify
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from datetime import datetime
import json
import os
import base64

app = Flask(__name__)

# MongoDB Configuration (Optional - will work without it)
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')

try:
    from pymongo import MongoClient
    
    
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()
    db = client['form_automation']
    forms_collection = db['forms']
    logs_collection = db['logs']
    MONGO_AVAILABLE = True
    print("✅ MongoDB Connected!")
except Exception as e:
    print(f"⚠️  MongoDB not available: {e}")
    print("⚠️  Running without database")
    client = None
    forms_collection = None
    logs_collection = None
    MONGO_AVAILABLE = False

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return str(obj)
        return super(JSONEncoder, self).default(obj)

app.json_encoder = JSONEncoder

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/forms', methods=['GET'])
def get_forms():
    """Get all saved forms"""
    try:
        forms = list(forms_collection.find({}, {'_id': 0}))
        return jsonify({'status': 'success', 'forms': forms})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/forms', methods=['POST'])
def create_form():
    """Create new form template"""
    try:
        data = request.json
        form_data = {
            'form_id': data['form_id'],
            'name': data['name'],
            'url': data['url'],
            'fields': data['fields'],
            'created_at': datetime.now().isoformat()
        }
        forms_collection.insert_one(form_data)
        
        log_entry = {
            'form_id': data['form_id'],
            'timestamp': datetime.now().isoformat(),
            'action': 'create',
            'status': 'success',
            'message': f"Form '{data['name']}' created"
        }
        logs_collection.insert_one(log_entry)
        
        return jsonify({'status': 'success', 'message': 'Form saved successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/forms/<form_id>', methods=['DELETE'])
def delete_form(form_id):
    """Delete form template"""
    try:
        result = forms_collection.delete_one({'form_id': form_id})
        
        if result.deleted_count > 0:
            log_entry = {
                'form_id': form_id,
                'timestamp': datetime.now().isoformat(),
                'action': 'delete',
                'status': 'success',
                'message': f"Form deleted"
            }
            logs_collection.insert_one(log_entry)
            
            return jsonify({'status': 'success', 'message': 'Form deleted'})
        else:
            return jsonify({'status': 'error', 'message': 'Form not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/scrape', methods=['POST'])
def scrape_form():
    """Scrape form fields from URL using Playwright"""
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            page = context.new_page()
            
            page.goto(url, wait_until='networkidle', timeout=30000)
            page.wait_for_timeout(2000)
            
            fields = page.evaluate("""
                () => {
                    const fields = [];
                    const allInputs = document.querySelectorAll('input, textarea, select');
                    
                    allInputs.forEach(input => {
                        if (input.type === 'hidden' || input.type === 'submit' || input.type === 'button') {
                            return;
                        }
                        
                        let selector = '';
                        if (input.id) {
                            selector = '#' + input.id;
                        } else if (input.name) {
                            selector = `[name="${input.name}"]`;
                        } else if (input.className) {
                            selector = '.' + input.className.split(' ')[0];
                        }
                        
                        let label = '';
                        if (input.id) {
                            const labelEl = document.querySelector(`label[for="${input.id}"]`);
                            if (labelEl) label = labelEl.textContent.trim();
                        }
                        
                        let options = [];
                        if (input.tagName.toLowerCase() === 'select') {
                            options = Array.from(input.options).map(opt => ({
                                value: opt.value,
                                text: opt.textContent.trim()
                            }));
                        }
                        
                        fields.push({
                            type: input.type || input.tagName.toLowerCase(),
                            name: input.name || input.id || '',
                            id: input.id || '',
                            selector: selector,
                            placeholder: input.placeholder || '',
                            label: label,
                            required: input.required || false,
                            options: options,
                            tagName: input.tagName.toLowerCase()
                        });
                    });
                    
                    return fields;
                }
            """)
            
            screenshot = page.screenshot(full_page=False)
            screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
            
            browser.close()
            
            log_entry = {
                'form_id': 'scrape',
                'timestamp': datetime.now().isoformat(),
                'action': 'scrape',
                'status': 'success',
                'message': f"Scraped {len(fields)} fields from {url}"
            }
            logs_collection.insert_one(log_entry)
            
            return jsonify({
                'status': 'success', 
                'fields': fields,
                'screenshot': screenshot_base64,
                'count': len(fields)
            })
            
    except PlaywrightTimeout:
        return jsonify({'status': 'error', 'message': 'Page load timeout. Please check the URL.'}), 400
    except Exception as e:
        log_entry = {
            'form_id': 'scrape',
            'timestamp': datetime.now().isoformat(),
            'action': 'scrape',
            'status': 'error',
            'message': f"Failed to scrape: {str(e)}"
        }
        logs_collection.insert_one(log_entry)
        
        return jsonify({'status': 'error', 'message': f'Error: {str(e)}'}), 400

@app.route('/api/fill', methods=['POST'])
def fill_form():
    """Automatically fill form using Playwright"""
    data = request.json
    form_id = data.get('form_id')
    form_values = data.get('values', {})
    
    form = forms_collection.find_one({'form_id': form_id}, {'_id': 0})
    if not form:
        return jsonify({'status': 'error', 'message': 'Form not found'}), 404
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            page = context.new_page()
            
            page.goto(form['url'], wait_until='networkidle', timeout=30000)
            page.wait_for_timeout(2000)
            
            filled_fields = []
            errors = []
            
            for field in form['fields']:
                selector = field.get('selector', '')
                field_name = field.get('name', '')
                field_type = field.get('type', '')
                value = form_values.get(field_name, '')
                
                if not selector or not value:
                    continue
                
                try:
                    page.wait_for_selector(selector, timeout=5000, state='visible')
                    
                    if field_type in ['select', 'select-one']:
                        page.select_option(selector, value)
                    elif field_type == 'checkbox':
                        if str(value).lower() in ['true', '1', 'yes', 'on']:
                            page.check(selector)
                    elif field_type == 'radio':
                        page.check(selector)
                    elif field_type == 'file':
                        continue
                    else:
                        page.fill(selector, str(value))
                    
                    filled_fields.append(field_name)
                    page.wait_for_timeout(500)
                    
                except Exception as e:
                    errors.append(f"{field_name}: {str(e)}")
            
            submit_clicked = False
            submit_selectors = [
                'button[type="submit"]',
                'input[type="submit"]',
                'button:has-text("Submit")',
                'button:has-text("Send")',
                'button:has-text("Continue")',
                '[type="submit"]'
            ]
            
            for selector in submit_selectors:
                try:
                    if page.locator(selector).count() > 0:
                        page.click(selector, timeout=3000)
                        submit_clicked = True
                        break
                except:
                    continue
            
            page.wait_for_timeout(3000)
            screenshot = page.screenshot(full_page=False)
            screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
            browser.close()
            
            log_entry = {
                'form_id': form_id,
                'timestamp': datetime.now().isoformat(),
                'action': 'fill',
                'status': 'success',
                'message': f"Filled {len(filled_fields)} fields",
                'filled_fields': filled_fields,
                'errors': errors,
                'values': form_values
            }
            logs_collection.insert_one(log_entry)
            
            return jsonify({
                'status': 'success',
                'message': f'Form filled successfully. Filled {len(filled_fields)} fields.',
                'filled_fields': filled_fields,
                'errors': errors,
                'submit_clicked': submit_clicked,
                'screenshot': screenshot_base64
            })
    
    except Exception as e:
        log_entry = {
            'form_id': form_id,
            'timestamp': datetime.now().isoformat(),
            'action': 'fill',
            'status': 'error',
            'message': str(e)
        }
        logs_collection.insert_one(log_entry)
        
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Get activity logs"""
    try:
        logs = list(logs_collection.find({}, {'_id': 0}).sort('timestamp', -1).limit(100))
        return jsonify({'status': 'success', 'logs': logs})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/logs', methods=['DELETE'])
def clear_logs():
    """Clear all logs"""
    try:
        logs_collection.delete_many({})
        return jsonify({'status': 'success', 'message': 'All logs cleared'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/test-connection', methods=['GET'])
def test_connection():
    """Test MongoDB and Playwright"""
    results = {
        'mongodb': False,
        'playwright': False,
        'timestamp': datetime.now().isoformat()
    }
    
    try:
        client.server_info()
        results['mongodb'] = True
    except Exception as e:
        results['mongodb_error'] = str(e)
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
            results['playwright'] = True
    except Exception as e:
        results['playwright_error'] = str(e)
    
    return jsonify(results)

if __name__ == '__main__':
    # Create indexes only if MongoDB is available
    if MONGO_AVAILABLE:
        try:
            forms_collection.create_index('form_id', unique=True)
            logs_collection.create_index('timestamp')
        except Exception as e:
            print(f"⚠️  Could not create indexes: {e}")
    
    print("=" * 60)
    print("🤖 Form Automation System")
    print("=" * 60)
    print(f"MongoDB: {'Connected' if MONGO_AVAILABLE else 'Not Available'}")
    print(f"Server: http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False, threaded=True)



