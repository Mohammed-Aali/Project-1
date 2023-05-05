import os 
import smtplib
from imghdr import what
from email.message import EmailMessage

# define sender, receiver, subject and message body
sender = os.environ.get('EMAIL_ADDRESS')
receiver = 'alalimohammed258@gmail.com'
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

msg = EmailMessage()
msg['Subject'] = 'Registration Confirmation'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'alalimohammed258@gmail.com'
msg.set_content(f"""<htm>
<h3>Thank you for registering with us. Your registration is now complete.<h3>

<p>👇👇👇Your confirmation code is 👇👇👇:</p>
                
                <h1>[Code]</h1>

<p>Please use this code to verify your account.</p>

<p>If you have any questions or concerns, please dont hesitate to contact us.</p>
<br><br>
<p>Best regards, 3effect team 👻</p>
</html>""")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
