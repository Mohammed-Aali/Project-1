import smtplib, os
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Generate a random code
code = random.randint(100000, 999999)

# Create the plain-text and HTML version of your message
text = f"Hi!\nHow are you?\nHere is your confirmation code:\n{code}"
html = f"""\
<html>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is your confirmation code:<br>
       <b>{code}</b>
    </p>
  </body>
</html>
"""

# Create a multipart message and set headers
message = MIMEMultipart("alternative")
message["Subject"] = "Email confirmation"
message["From"] = os.environ.get('EMAIL_ADDRESS')
message["To"] = "alalimohammed258@gmail.com"

# Add both plain-text and HTML parts to the message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

with smtplib.SMTP("localhost") as server:
    server.sendmail(
        "sender@example.com", "recipient@example.com", message.as_string()
    )