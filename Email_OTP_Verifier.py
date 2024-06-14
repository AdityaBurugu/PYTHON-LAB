import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender_email, sender_password)

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Create the body of the message (a plain-text and an HTML version).
    text = message
    html = """\
    <html>
      <body>
        <p>{}</p>
      </body>
    </html>
    """.format(message)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via the SMTP server.
    smtp_server.sendmail(sender_email, recipient_email, msg.as_string())

    # Quit SMTP session
    smtp_server.quit()

# Example usage
if __name__ == "__main__":
    sender_email = 'adityaburugu1234567@gmail.com'
    sender_password = 'ykro xwxk jvtn pxgz'
    recipient_email = 'adityaburuguofficial@gmail.com'
    subject = 'OTP Verification'
    otp=str(random.randint(1000,9999))
    message = 'Your OTP is {}'.format(otp)

    send_email(sender_email, sender_password, recipient_email, subject, message)

    OTP_Verify = input("Enter Your OTP:")
    if otp==OTP_Verify:
        print("Successful")
    else:
        print("Invalid OTP")