import os 
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = "Check out Brons as a Puppy"
msg["From"] = EMAIL_ADDRESS
msg["To"] = 'alalimohammed258@gmail.com'
msg.set_content("Image_attached...")

print(os.listdir())
print(os.getcwd())
print(os.chdir(static))

with open(r"C:\Users\Ghost\Project-1\static\images\butterfly_copy.jpg", 'rb') as f:
    file_data = f.read() 
    file_type = imghdr.what(f.name)

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     smtp.send_message(msg)
