import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from forecast import config


class SendMail:

    def __init__(self):
        self.__email = config.EMAIL_ADDRESS
        self.__password = config.PASSWORD

    def send_mail(self,target, subject, msg):
        try:
            content = MIMEMultipart()
            content['From'] = self.__email
            content['To'] = target
            content['Subject'] = subject

            content.attach(
                MIMEText(msg, 'plain')
            )

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.__email, self.__password)
            server.sendmail(self.__email, target, content.as_string())
            server.quit()

            print("Email has been sent")
        except:
            print("Couldn't send an email")