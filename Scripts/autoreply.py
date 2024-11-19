import imaplib
import smtplib
from email.mime.text import MIMEText

def auto_reply():
    # Connect to email server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login('youremail@gmail.com', 'yourpassword')
    mail.select('inbox')

    # Search for unread emails
    status, emails = mail.search(None, 'UNSEEN')

    if status == "OK":
        for email_id in emails[0].split():
            status, email_data = mail.fetch(email_id, '(RFC822)')
            email_msg = email_data[0][1].decode('utf-8')

            # Send auto-reply
            send_email("Auto-reply", "Thank you for your email. I'll get back to you soon.", 'sender@example.com')

def send_email(subject, body, to_email):
    sender_email = 'youremail@gmail.com'
    sender_password = 'yourpassword'
    receiver_email = to_email

    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

auto_reply()