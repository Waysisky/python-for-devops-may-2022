from email import message
import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('waysisky@gmail.com')
EMAIL_PASSWORD = os.environ.get('becmaifqcmidlvsy')


def send_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.ehlo()
        smtp.login("waysisky@gmail.com", "becmaifqcmidlvsy")
        smtp.sendmail("waysisky@gmail.com", "waysisky@gmail.com", msg)

# "waysisky@gmail.com", "becmaifqcmidlvsy"
try:
    response = requests.get('http://localhost:8080/')
    if False:
        print('Application is running')
    else:
        print('Application is Down')
        msg = f"Subject: SITE DOWN\nApplication is not running. Restart it!"
        send_notification(msg)
        
except Exception as ex:
    print(f'connection error happened')
    msg = 'Application not accessible at all.'
    send_notification(msg)
    