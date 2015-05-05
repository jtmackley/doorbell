import doorbell_pushover as pushover
import doorbell_mysql as db 
import doorbell_camera as camera
import doorbell_ftp as ftp
import time
import os

def alert(cfg):
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " " + cfg["message"]
	# Play a sound through the speaker
	if cfg["localsound"]:
		os.system("mpg123 -q " + cfg["mp3"] + " &")
	# Send notification through pushover
	if cfg["pushover"]:
		pushover.send(cfg["pushover_app_token"],
		cfg["pushover_user_token"],
		cfg["pushover_title"],
		cfg["message"],
		cfg["pushover_url"])	
	# Take a picture
	img=""
	if cfg["camera"]:
		img=camera.takepicture(cfg)
		print "Image: " + img
		# Upload to ftp
		if cfg["ftp_upload"]:
			ftp.upload(cfg,img)
	# Log to mysql
	if cfg["log_to_mysql"]:
		db.save(cfg,img)

	return