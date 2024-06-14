import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
logging.basicConfig(level=logging.INFO)

def load_configuration():
    """Load configuration from a file or environment variables."""
    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_username = os.environ.get('SMTP_USERNAME', 'adityaburugu1234567@gmail.com')
    smtp_password = os.environ.get('SMTP_PASSWORD', 'ykro xwxk jvtn pxgz')

    from_email = os.environ.get('FROM_EMAIL', 'adityaburugu1234567@gmail.com')
    to_email = os.environ.get('TO_EMAIL', 'adityaburuguofficial@gmail.com')

    return smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email

def create_email_message(from_email, to_email, subject, body, files):
    """Create a MIME multipart email message with attachments."""
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    for file_path in files:
        with open(file_path, 'rb') as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
            msg.attach(attachment)

    return msg

def send_email(smtp_server, smtp_port, smtp_username, smtp_password, msg):
    """Send the email using SMTP."""
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.send_message(msg)
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error("An error occurred while sending the email: %s", e)

def main():
    smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email = load_configuration()

    subject = 'Permission'
    body = 'Please find attached the report.\nThankyou'
    files = ["ADD.py", "demo.txt", "Permission.docx"]

    msg = create_email_message(from_email, to_email, subject, body, files)
    send_email(smtp_server, smtp_port, smtp_username, smtp_password, msg)

if __name__ == "__main__":
    main()