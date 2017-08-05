FROM_ADDR = 'Zsolt Horvat <zshorvat@cisco.com>'
TO_ADDR = 'ask-wnbu-pm@cisco.com'
BCC_ADDR = 'group.crobbins@cisco.com'
REPLY_TO_ADDRESS = 'Zsolt Horvat <group.crobbins@cisco.com>'
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

s = smtplib.SMTP('outbound.cisco.com', 25)
s.sendmail(FROM_ADDR, TO_ADDR, msg.as_string())
s.quit()
