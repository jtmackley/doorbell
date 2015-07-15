import httplib, urllib

def send(cfg,action):
	if (len(cfg["pushover_app_token"])>0) and (len(cfg["pushover_user_token"])>0):
		print "Sending to pushover..."
		# Start your connection with the Pushover API server
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		# Send a POST request in urlencoded json
		conn.request("POST", "/1/messages.json",
		urllib.urlencode({
		"token": cfg["pushover_app_token"],
		"user": cfg["pushover_user_token"],
		"title": cfg["pushover_title"] + " " + ("Button" if action==1 else "Sensor"),
		"message": cfg["app_message"],
		"url": cfg["pushover_url"],
		}), { "Content-type": "application/x-www-form-urlencoded" })

		# Listen for any error messages or other responses
		return conn.getresponse()
