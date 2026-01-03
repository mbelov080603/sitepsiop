# PSIOP Landing Page - Flask Application
#
# Installation and running:
# 1. Create and activate virtual environment:
#    python3 -m venv venv
#    source venv/bin/activate  (or venv\Scripts\activate on Windows)
# 2. Install dependencies:
#    pip install -r requirements.txt
# 3. Run the application:
#    python app.py
# 4. Open in browser:
#    http://127.0.0.1:5000/

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'psiop_secret_key_2025_neurointerface'

DB_NAME = 'leads.db'


def get_db_connection():
    """Create database connection"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database and create leads table if not exists"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT,
            usage TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' initialized successfully")


@app.route('/')
def index():
    """Render main landing page"""
    return render_template('index.html', success=False, error=None, form_data={})


@app.route('/lead', methods=['POST'])
def lead():
    """Handle lead form submission"""
    # Get form data
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    role = request.form.get('role', '').strip()
    usage = request.form.get('usage', '').strip()
    
    # Store form data to repopulate on error
    form_data = {
        'name': name,
        'email': email,
        'role': role,
        'usage': usage
    }
    
    # Validate required fields
    if not name:
        return render_template('index.html', 
                             success=False, 
                             error='Пожалуйста, укажите ваше имя',
                             form_data=form_data)
    
    if not email:
        return render_template('index.html', 
                             success=False, 
                             error='Пожалуйста, укажите ваш email',
                             form_data=form_data)
    
    # Basic email validation
    if '@' not in email or '.' not in email.split('@')[-1]:
        return render_template('index.html', 
                             success=False, 
                             error='Пожалуйста, укажите корректный email адрес',
                             form_data=form_data)
    
    # Save to database
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            INSERT INTO leads (name, email, role, usage, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, role, usage, created_at))
        
        conn.commit()
        conn.close()
        
        # Success - return page with success message and empty form
        return render_template('index.html', 
                             success=True, 
                             error=None,
                             form_data={})
    
    except Exception as e:
        print(f"Database error: {e}")
        return render_template('index.html', 
                             success=False, 
                             error='Произошла ошибка при сохранении заявки. Попробуйте позже.',
                             form_data=form_data)


@app.route('/download-onepager')
def download_onepager():
    """Handle one-pager download"""
    try:
        return send_file('static/PSIOP_OnePager.pdf', 
                        as_attachment=True, 
                        download_name='PSIOP_OnePager.pdf',
                        mimetype='application/pdf')
    except Exception as e:
        print(f"Download error: {e}")
        return redirect(url_for('index'))


@app.route('/admin/leads')
def admin_leads():
    """View all lead submissions (admin only)"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, name, email, role, usage, created_at 
            FROM leads 
            ORDER BY created_at DESC
        ''')
        leads = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries for easier handling
        leads_data = []
        for lead in leads:
            leads_data.append({
                'id': lead['id'],
                'name': lead['name'],
                'email': lead['email'],
                'role': lead['role'],
                'usage': lead['usage'],
                'created_at': lead['created_at']
            })
        
        return render_template('admin_leads.html', leads=leads_data)
    
    except Exception as e:
        print(f"Error fetching leads: {e}")
        return f"Error: {e}"


if __name__ == '__main__':
    # Initialize database before running the app
    init_db()
    
    # Run Flask development server
    app.run(debug=True, host='127.0.0.1', port=5000)

