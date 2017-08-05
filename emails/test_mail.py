'''
https://docs.python.org/3/library/email-examples.html
'''
# import smtplib
# server = smtplib.SMTP('outbound.cisco.com', 25)


# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'insert smtp server FQDN or IP'


COMMASPACE = ', '
IMG = 'jon_snow.jpg'

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Test python'
TO_ADDR = 'ariastark@cisco.com'
FROM_ADDR = 'jonsnow@cisco.com'
BCC_ADDR = 'vodka@cisco.com'
REPLY_TO_ADDRESS = 'Jon Snow <knowsnothing@cisco.com>'

msg['From'] = FROM_ADDR
# msg['To'] = COMMASPACE.join(family)
msg['To'] = TO_ADDR
msg['Bcc'] = BCC_ADDR
msg.add_header('reply-to', REPLY_TO_ADDRESS)
msg.preamble = 'Test'
body =  MIMEText('This is a test')
msg.attach(body)
with open(IMG, 'rb') as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)

#
# # Assume we know that the image files are all in PNG format
# for file in pngfiles:
#     # Open the files in binary mode.  Let the MIMEImage class automatically
#     # guess the specific image type.
#     with open(file, 'rb') as fp:
#         img = MIMEImage(fp.read())
#     msg.attach(img)

# Send the email via our own SMTP server.
s = smtplib.SMTP(SMTP_SERVER, 25)
s.send_message(msg)
s.quit()