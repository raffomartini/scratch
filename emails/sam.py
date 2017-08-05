import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


TO_ADDR = 'ask-wnbu-pm@cisco.com'
FROM_ADDR = 'Samuel Ribeiro <sacorrei@cisco.com>'
BCC_ADDR = 'group.crobbins@cisco.com'
REPLY_TO_ADDRESS = 'Samuel Ribeiro <group.crobbins@cisco.com>
SUBJECT = "R: Re: ping"

TEXT = '''\
Why I am receiving this?
Unsuscribe me.
'''

part1 = MIMEText(TEXT, 'plain')


msg = MIMEMultipart('Alternative')

msg['Subject'] = SUBJECT
msg['From'] = FROM_ADDR
msg['To'] = TO_ADDR
msg['Bcc'] = BCC_ADDR
msg.add_header('reply-to', REPLY_TO_ADDRESS)

msg.attach(part1)

s = smtplib.SMTP('outbound.cisco.com', 25)
s.sendmail(FROM_ADDR, TO_ADDR, msg.as_string())
s.quit()
