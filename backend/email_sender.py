# email_sender.py

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()  # ✅ This line loads the .env file

def send_email(to_email, subject, content):
    """
    Sends an email using SendGrid
    """
    try:
        message = Mail(
            from_email='tanishqchavan241@gmail.com',
            to_emails=to_email,
            subject=subject,
            html_content=content
        )

        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))  # Uses key loaded from .env
        response = sg.send(message)
        print(f"✅ Email sent to {to_email}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email to {to_email}: {e}")
