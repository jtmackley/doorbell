import doorbell_pushover as pushover
import time
import os

def alert(cfg):
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " " + cfg["message"]
	# Play a sound through the speaker
	os.system("mpg123 -q " + cfg["mp3"] + " &")
	# Send notification through pushover
	if cfg["pushover"]:
		pushover.send(cfg["pushover_app_token"],
		cfg["pushover_user_token"],
		cfg["pushover_title"],
		cfg["message"],
		cfg["pushover_url"])	

	return