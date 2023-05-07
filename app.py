import re, os
from cs50 import SQL
from flask import Flask, render_template, flash, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology

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

@app.route('/')
def index():
    """Display Projects"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log user in"""

    # forgets any user_id
    session.clear()

    

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register user"""
    if request.method == 'POST':
        # set up the variables
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirmation')

        # set up regexp for checks
        password_regexp = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,32}$"
        email_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

        # check vairables
        check_email_regexp = re.search(email_regex, email)
        check_password_regexp = re.search(password_regexp, password)

        # go to confirm page for code
        if not check_password_regexp:
            return apology('Always has been', 'Invalid Password')
        elif not check_email_regexp:
            return apology("Always has been",'Invalid Email')
        else:
            return redirect('/confirm')
    else:
        print('bye')
        return render_template('register.html')

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        return apology('confirmation is a success', 404)
    else:
        return render_template("confirm.html")

@app.route('/logout')
def logout():
    """ Log user out """

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect('/login')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
