from flask import Flask, redirect, url_for, render_template

# configure application
app = Flask(__name__)

# set home page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # automate the detection of changes in the server side, meaning I won't have to reload everytime I have to see changes
    app.run(debug=True)