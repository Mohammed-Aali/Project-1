import os 
import smtplib
import random, string
from email.message import EmailMessage

# generates a random code for conformation
code = "".join(random.choices(string.ascii_letters + string.digits, k=6))

# define sender, receiver, subject and message body
sender = os.environ.get('EMAIL_ADDRESS')
receiver = 'alalimohammed258@gmail.com'
password = os.environ.get('EMAIL_PASSWORD')
subject = 'Registration Confirmation'
message_body = f"""<htm>
<h3>Thank you for registering with us. Your registration is now complete.</h3>

<p style="text-align:center">👇👇👇Your confirmation code is 👇👇👇:</p>
                
                <h1 style="text-align:center">{code}</h1>

<p>Please use this code to verify your account.</p>

<p>If you have any questions or concerns, please dont hesitate to contact us.</p>

<p>Best regards, 3ffect team 👻.</p>
</htm>"""

# create an EmailMessage object
msg = EmailMessage()
msg['Subject'] = 'Registration Confirmation'
msg['From'] = sender
msg['To'] = 'alalimohammed258@gmail.com'

# set the msg body as html
msg.set_content(message_body, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
