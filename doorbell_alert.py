import doorbell_pushover as pushover
import time
import os

def alert():
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " Doorbell!"
	# Play a sound through the speaker
	os.system('mpg123 -q /home/pi/doorbell/bell.mp3 &')
	# Send notification through pushover
	pushover.send("Doorbell"
	,"Doorbell rang at: " + (time.strftime("%d/%m/%Y %H:%M:%S")),
	"http://2seven.co.uk/doorbell")	
	return
