import time
import os

def alert(cfg):
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " " + cfg["app_message"]
	# Play a sound through the speaker
	if cfg["mp3"]:
		os.system("mpg123 -q " + cfg["mp3file"] + " &")
	# Send notification through pushover
	if cfg["pushover"]:
		import doorbell_pushover as pushover
		pushover.send()	
	# Take a picture
	img=""
	if cfg["camera"]:
		import doorbell_camera as camera
		img=camera.takepicture(cfg)
		print "Image: " + img
		# Upload to ftp
		if cfg["ftp"]:
			import doorbell_ftp as ftp
			ftp.upload(cfg,img)
	# Log to mysql
	if cfg["mysql"]:
		import doorbell_mysql as db 
		db.save(cfg,img)
	# Log to email
	if cfg["email"]:
		import doorbell_email as email 
		email.mail(cfg,img)

	return