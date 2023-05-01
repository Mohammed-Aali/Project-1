from cs50 import SQL
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


# set up our database
db = SQL('sqlite:///users.db')

# configure application
app = Flask(__name__)

# set secret key
app.secret_key = 'hello'

# set lifetime of data
app.permanant_session_lifetime = timedelta(days=1000)

# set home page
@app.route('/')
def index():
    return render_template('index.html')

#test for now
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanant = True
        user = request.form['username']
        session['user'] = user
        flash('Login is successful!', 'info')
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            email = request.form.get('email')
            session['email'] = email
            flash('email is submitted', 'info')
        else:
            if 'email' in session:
                email = session['email']
    
        return render_template('user.html', email=email)
    else:
        flash('You are not logged in', 'info')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user' in session:
        flash(f'{session.get("user")} has logged out successfully', 'info')
        session.pop('user', None)
        session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # automate the detection of changes in the server side, meaning I won't have to reload everytime I have to see changes
    app.run(debug=True)