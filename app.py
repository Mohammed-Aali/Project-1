import re
import sqlite3

from cs50 import SQL
from flask import Flask, url_for, render_template, flash, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, generate_code, register_required, send_email

# configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL('sqlite:///website.db')

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
@app.route('/home/')
def index():
    """Display Projects"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log user in"""

    # forgets any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("email"):
            return render_template("login.html", msg=msg)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html", msg=msg)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("login.html", msg=msg)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register user"""
    if request.method == 'POST':
        # set up the variables
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirmation')
        msg = 'Email is already in use'

        # check if email exist in our data base
        row = db.execute("SELECT email FROM users WHERE email = ?", email )

        if len(row) > 0:
            return render_template('register.html', msg=msg)
            
        # set up regexp for checks
        password_regexp = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,32}$"
        email_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

        # check vairables
        check_email_regexp = re.search(email_regex, email)
        check_password_regexp = re.search(password_regexp, password)

        # check for code confirmation and
        if not check_password_regexp:
            return apology('Invalid Password', 'Valid Password')
        elif not check_email_regexp:
            return apology("Invalid Email",'Valid Email')
        elif str(confirm) != str(password):
            return apology('invalid Confirmation','Valid Confirmation')
        else:
            hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            session['password'] = hash_password
            session['email'] = email
            session['code'] = generate_code(6)
            send_email(email, session.get('code'))

            return redirect('/confirm')
    else:
        return render_template('register.html')

@app.route('/confirm', methods=['GET', 'POST'])
@register_required
def confirm():
    if request.method == 'POST':
        # set up the variabes
        confirm_code = request.form.get('confirmationCode')
        email = session.get('email', None)
        code = session.get('code', None)
        password = session.get('password', None)
        msg = "<div class='invalid-feedback pt-1 d-block' role='alert'> Please enter a valid confirmation code. </div>"
        
        # incase we could not send the code
        if code == None or email == None or password == None:
            return apology('Easy regestration?', 'We encountered an error oops!')
            session.clear()
            flash('Oopsie! we have to register you again 😞')

        # compare confirm code againts random code
        if (str(code.lower()) != str(confirm_code.lower())):
            return render_template('confirm.html', msg=msg)
        else:
            # add to database
            try:
                db.execute('INSERT INTO users (email, hash) VALUES (?, ?)', email, password)
            except sqlite3.IntegrityError as err:
                return apology('Your data going into our database', f'{err}')
                session.clear()
                flash('Oopsie! we have to register you again 😞')
            
            flash('Your registration was successful 👍')
            return redirect('/')
    else:
        return render_template("confirm.html")

@app.route('/logout')
def logout():
    """ Log user out """

    # forget any user_id
    session.clear()

    # redirect user to front page
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
