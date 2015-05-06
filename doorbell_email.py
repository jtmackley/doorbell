#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

def mail(cfg,img):
   print "Sending email to " + cfg["email_to"] + "..."
   msg = MIMEMultipart()

   msg['From'] = cfg["email_account_user"]
   msg['To'] = cfg["email_to"]
   msg['Subject'] = cfg["email_subject"]

   msg.attach(MIMEText(cfg["app_message"]))
   attach=cfg["camera_local_file_path"] + img
   part = MIMEBase('application', 'octet-stream')
   if len(img)>0:
      part.set_payload(open(attach, 'rb').read())
      Encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
      msg.attach(part)

   mailServer = smtplib.SMTP(cfg["email_server"], cfg["email_port"])
   mailServer.ehlo()
   if cfg["email_tls"]:
      mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(cfg["email_account_user"], cfg["email_account_password"])
   mailServer.sendmail(cfg["email_account_user"], cfg["email_to"], msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()