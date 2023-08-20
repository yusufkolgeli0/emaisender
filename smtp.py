import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "ysfklgl645@gmail.com"
recipients = ["ramazancetinn@yandex.com", "ysfklgl645@gmail.com"]
password = "bumrbjkxlvwmbhsj"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # gmail smpt connection 
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail_server.login(sender, password)

    # send mail
    mail_server.sendmail(sender, recipients, msg.as_string())


    print("Message sent!")


send_email(subject, body, sender, recipients, password)