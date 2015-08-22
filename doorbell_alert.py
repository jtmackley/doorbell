import time
import os

def alert(cfg,action):
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " " + cfg["app_message"]

	img=""
	# Take a picture
	if (cfg["camera"] & action):
		import doorbell_camera as camera
		img=camera.takepicture(cfg)
		print "Image: " + img
	# Play a sound through the speaker
	if (cfg["mp3"] & action):
		os.system("mpg123 -q " + cfg["mp3file"] + " &")
	# Send notification through pushover
	if (cfg["pushover"] & action):
		import doorbell_pushover as pushover
		pushover.send(cfg,action)	
	if (cfg["pushbullet"] & action):
		import doorbell_pushbullet as pbullet
		pbullet.send(cfg,action)	
	# Upload to ftp
	if (cfg["ftp"] & action):
		import doorbell_ftp as ftp
		ftp.upload(cfg,img)
	# Log to mysql
	if (cfg["mysql"] & action):
		import doorbell_mysql as db 
		db.save(cfg,img)
	# Log to email
	if (cfg["email"] & action):
		import doorbell_email as email 
		email.mail(cfg,img)

	# Delet any temp image
	try:
		os.remove(cfg["camera_local_file_path"] + img)
	except OSError:
		pass

	print "Waiting..."
		
	return