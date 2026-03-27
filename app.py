import csv
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='Static', template_folder='Templates')
BASE_DIR = Path(__file__).resolve().parent
CONTACTS_CSV = BASE_DIR / 'contacts.csv'
CONTACTS_TXT = BASE_DIR / 'contacts.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/greet/<name>/<name2>')
def greet(name, name2):
    return f'Hello {name} and {name2}, welcome to our website!'

@app.route('/Category1/<name3>/<name4>')
def Category1(name3, name4):
    return f'Hello {name3} and {name4}, welcome to our website!'

@app.route('/showdetails/<category>/<int:product_id>')
def showdetails(category, product_id):
    return f'Showing details for {category} with ID {product_id}'

# ONLY ONE contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip() or 'Traveler'
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Save to CSV
        with open(CONTACTS_CSV, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, message])

        # Save to TXT
        with open(CONTACTS_TXT, 'a', encoding='utf-8') as f:
            f.write(f"Name: {name}, Email: {email}, Message: {message}\n")

        return render_template('contact_success.html', name=name)

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
