from celery import Celery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import logging

app = Celery('task', broker='redis://localhost:6379')

logger = logging.getLogger(__name__)


@app.task()
def hello():
    with open('test.txt', 'r') as f:
        f.write('h')


@app.task()
def send_verification(text="aa"):
    try:
        sender = 'Library Manager'
        receiver = "1.ibragimovvvvv@gmail.com"
        code = text
        subject = 'Salom'
        body = f'{code}'

        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        username = "1.ibragimovvvvv@gmail.com"
        password = "ivkd cqhn xnzc cikw"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False
