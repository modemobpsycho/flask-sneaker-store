import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from website.config import Config


def send_email(to, subject, template):
    smtp_server = Config.MAIL_SERVER
    smtp_port = Config.MAIL_PORT
    smtp_username = Config.MAIL_USERNAME
    smtp_password = Config.MAIL_PASSWORD

    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = to
    msg["Subject"] = subject

    body = MIMEText(template, "html")
    msg.attach(body)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to, msg.as_string())
        server.quit()
    except Exception as e:
        print("Failed to send email:", str(e))
