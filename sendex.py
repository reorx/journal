#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(text, html):
    address_book = ['reorxmeng@sohu-inc.com']
    sender = 'reorxmeng@sohu-inc.com'
    subject = "My subject"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')

    msg['From'] = sender
    msg['To'] = ','.join(address_book)
    msg['Subject'] = subject

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    msg_str = msg.as_string()
    #print msg_str

    smtp = smtplib.SMTP('mail.sohu-inc.com')
    smtp.login('reorxmeng', base64.b64decode('bXgzMjBTT0hVMg=='))
    smtp.sendmail(sender, address_book, msg_str)
    smtp.quit()
