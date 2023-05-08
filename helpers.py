import random, string, secrets, os, smtplib

from email.message import EmailMessage
from flask import render_template, session, redirect
from functools import wraps

# this code snippet is from cs50x final project finance
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

# this code snippet is also from cs50x final project finance
def register_required(f):
    """
    Decorate routes to require registration.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("email") is None:
            return redirect("/register")
        return f(*args, **kwargs)
    return decorated_function

# this code generates a string of chars and digits that is six chars long
def generate_code(length):
    code = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for x in range(length))
    return str(code) 

# this code sends an email to the users email for confimation 
def send_email(receiver, code):

    # define sender, receiver, subject and message body
    sender = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')
    subject = 'Your registration confirmation'
    message_body = f"""<html>
    <h3>Hello, and thank you for signing up with us</h3>

    Please copy the code below and paste it into your browser to confirm your email address, and activate your account.
    

    <div style="text-align:center">

        <p>👇👇👇Your confirmation code is 👇👇👇:</p>
                    
                    <h1>{code}</h1>
    </div>

    
    <p> If you did not sign up with us, please ignore this email. This may have been a mistake or a fraudulent attempt to use your email address. </p>

    <p>Best regards, 3ffect team 👻.</p>
    </html>"""

    # create an EmailMessage object
    msg = EmailMessage()
    msg['Subject'] = 'Registration Confirmation'
    msg['From'] = sender
    msg['To'] = receiver

    # set the msg body as html
    msg.set_content(message_body, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Successfully sent email")
    except socket.error as e:
        return apology(f"Could not connect to server - is it down? ({e.errno}): {e.strerror}")

    except smtplib.SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        return apology(f"Server returned an error code: {error_code}", error_message)
