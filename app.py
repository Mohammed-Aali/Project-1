from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

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
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user' in session:
        flash(f'{session.get("user")} has logged out successfully', 'info')
        session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # automate the detection of changes in the server side, meaning I won't have to reload everytime I have to see changes
    app.run(debug=True)