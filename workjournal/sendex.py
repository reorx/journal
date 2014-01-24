#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, text, html):
    username = raw_input('username:')
    password = getpass.getpass('password:')
    send_to = raw_input('send to:')

    sender = '%s@sohu-inc.com' % username
    address_book = [send_to]

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
    smtp.login(username, password)
    smtp.sendmail(sender, address_book, msg_str)
    smtp.quit()


if __name__ == '__main__':
    send_email('test', 'hello', '<html><body><h1>HELLO</h1></body></html>')
