from pushbullet import Pushbullet

def send(cfg,action):
	if (len(cfg["pushbullet_app_token"])>0):
		print "Sending to pushbullet..."
		pb=Pushbullet(cfg["pushbullet_app_token"])
		push = pb.push_link(cfg["pushover_title"] + " " + ("Button" if action==1 else "Sensor"), "http://www.2seven.co.uk/doorbell")	

		# Listen for any error messages or other responses
		return push
