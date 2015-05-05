import httplib, urllib

def send(app_token,user_token,title,message,url):
	if (len(app_token)>0) and (len(user_token)>0):
		print "Sending to pushover..."
		# Start your connection with the Pushover API server
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		# Send a POST request in urlencoded json
		conn.request("POST", "/1/messages.json",
		urllib.urlencode({
		"token": app_token,
		"user": user_token,
		"title": title,
		"message": message,
		"url": url,
		}), { "Content-type": "application/x-www-form-urlencoded" })

		# Listen for any error messages or other responses
		return conn.getresponse()
