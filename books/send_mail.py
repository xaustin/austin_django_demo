# -*- coding: utf-8 -*-
__author__ = '许仕强'
# @Time    : 2018/8/27 15:24
# @Email   : austin@canway.net


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.utils import COMMASPACE


def send_mail(smtp_host, smtp_port, smtp_user, smtp_pwd, smtp_usessl, smtp_usetls, mail_sender, receiver):
    print("1. build mail content")
    # Create message container
    msg = MIMEMultipart()
    msg['Subject'] = "This is a test email"
    msg['From'] = mail_sender
    msg['To'] = COMMASPACE.join(receiver)
    html = "Hello world!"
    part2 = MIMEText(html, 'html', 'utf-8')
    msg.attach(part2)

    print("2. connect smtp client")
    if smtp_usessl:
        smtp = smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=10)
    else:
        smtp = smtplib.SMTP(smtp_host, smtp_port, timeout=10)

    if smtp_usetls:
        smtp.set_debuglevel(True)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

    print("3. login via username/password")
    smtp.ehlo()
    smtp.starttls()
    smtp.login(smtp_user, smtp_pwd)

    print("4. do send mail")
    smtp.sendmail(mail_sender, receiver, msg.as_string())

    smtp.quit()
    print("5. done")
    return True


def main():

    smtp_host = "smtp.sohu.com"
    smtp_port = 465

    # smtp_user = "1922878025@qq.com"
    # smtp_pwd = "hirsfmozdafbdcac"

    smtp_user = "smtp.sohu.com"
    smtp_pwd = "116131xsq"

    smtp_usessl = True
    smtp_usetls = False

    mail_sender = "1922878025@qq.com"
    receiver = ["2020456654@qq.com", "1734917@qq.com", "553109876@qq.com"]

    send_mail(smtp_host, smtp_port, smtp_user, smtp_pwd, smtp_usessl, smtp_usetls, mail_sender, receiver)


if __name__ == '__main__':

    main()
