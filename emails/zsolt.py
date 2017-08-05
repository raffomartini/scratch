# Python 2.7.1

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'insert smtp server FQDN or IP'

FROM_ADDR = 'Zsolt Horvat <zshorvat@fiasco.com>'
TO_ADDR = 'chaos@fiasco.com'
BCC_ADDR = 'large-group@fiasco.com'
REPLY_TO_ADDRESS = 'Zsolt Horvat <large-group@fiasco.com>'
SUBJECT = "R: UNSUSCRIBE ME! R: Re: ping"

TEXT = '''\
+1 '''

part1 = MIMEText(TEXT, 'plain')


msg = MIMEMultipart('Alternative')

msg['Subject'] = SUBJECT
msg['From'] = FROM_ADDR
msg['To'] = TO_ADDR
msg['Bcc'] = BCC_ADDR
msg.add_header('reply-to', REPLY_TO_ADDRESS)

msg.attach(part1)

s = smtplib.SMTP(SMTP_SERVER, 25)
s.sendmail(FROM_ADDR, TO_ADDR, msg.as_string())
s.quit()
