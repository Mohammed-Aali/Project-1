from cs50 import SQL
from flask import Flask, render_template, flash, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL('sqlite:///portfolio.db')

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


subject = 'Registration Confirmation'
body = """ 
Thank you for registering with us. Your registration is now complete.

Your confirmation code is: [Code]

Please use this code to verify your account.

If you have any questions or concerns, please don’t hesitate to contact us.

Best regards, Mohammed 
"""
password = os.environ.get('EMAIL_PASSWORD')


@app.route('/')
def index():
    """Display Projects"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
