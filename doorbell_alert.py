import doorbell_pushover as pushover
import time
import pyglet

def alert():
	# Output to Local Screen
	print (time.strftime("%d/%m/%Y %H:%M:%S")) + " Doorbell!"
	# Play a sound through the speaker
	bell = pyglet.media.load('bell.wav', streaming=False)
	bell.play()
	# Send notification through pushover
	pushover.send("Doorbell"
	,"Doorbell rang at: " + (time.strftime("%d/%m/%Y %H:%M:%S")),
	"http://2seven.co.uk/doorbell")	
	return
