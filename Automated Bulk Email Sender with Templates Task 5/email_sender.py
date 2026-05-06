import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, receiver, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)

        server.send_message(msg)
        server.quit()

        return "Sent"

    except Exception as e:
        return f"Failed: {e}"