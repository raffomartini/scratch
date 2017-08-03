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


COMMASPACE = ', '
IMG = 'jon_snow.jpg'

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Test python'
from_address = 'jsnow@cisco.com'
to_address = 'raffaello.martini@gmail.com'
bcc_address = 'martini@cisco.com'
REPLY_TO_ADDRESS = 'knowsnothing@cisco.com'

msg['From'] = from_address
# msg['To'] = COMMASPACE.join(family)
msg['To'] = to_address
msg['Bcc'] = bcc_address
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
s = smtplib.SMTP('outbound.cisco.com', 25)
s.send_message(msg)
s.quit()