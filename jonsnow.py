#!/usr/bin/env python3

import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

IMG = 'jon_snow.jpg'
TO_ADDR = 'raffaello.martini@gmail.com'
FROM_ADDR = 'jonsnow@cisco.com'
BCC_ADDR = 'martini@cisco.com'
REPLY_TO_ADDRESS = 'knowsnothing@cisco.com'

# Create the base text message.
msg = EmailMessage()
msg['Subject'] = "Brace yourself"
msg['From'] = FROM_ADDR
msg['To'] = TO_ADDR
msg['Bcc'] = BCC_ADDR
msg.add_header('reply-to', REPLY_TO_ADDRESS)
msg.set_content("""\
Brace yourself""")

# Add the html version.  This converts the message into a multipart/alternative
# container, with the original text message as the first part and the new html
# message as the second part.
meme_cid = make_msgid()
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Salut!<\p>
    <p>Cela ressemble à un excellent
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718>
            recipie
        </a> déjeuner.
    </p>
    <img src="cid:{meme_cid}" \>
  </body>
</html>
""".format(meme_cid=meme_cid[1:-1]), subtype='html')
# note that we needed to peel the <> off the msgid for use in the html.

# Now add the related image to the html part.
with open(IMG, 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=meme_cid)

# Send the message via local SMTP server.
with smtplib.SMTP('outbound.cisco.com', 25) as s:
    s.send_message(msg)