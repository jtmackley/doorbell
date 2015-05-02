import doorbell_pushover as pushover
import time

def alert():
        print (time.strftime("%d/%m/%Y %H:%M:%S")) + " Doorbell!"
	pushover.send("Doorbell"
	,"Doorbell rang at: " + (time.strftime("%d/%m/%Y %H:%M:%S")),
	"http://2seven.co.uk/doorbell")
	return
