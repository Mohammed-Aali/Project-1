from flask import Flask, redirect

# configure application
app = Flask(__name__)

# set home page
@app.route('/')
def index():
    return f'Hello and welcome to our humble site'

# set users page
@app.route('/<name>')
def user(name):
    return f'Hello, {name}'

# set admin page
@app.route('/admin')
def admin():
    return redirect('/')

if __name__ == '__main__':
    app.run()