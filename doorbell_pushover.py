import httplib, urllib

# Application specific variables
application_token = "aUxbrwySTK3exBeGaxch6yM44i9AZn"
user_token = "utthRauFAC3h8Ri2voU35VKkvRcyeL"

def send(title,message,url):
	# Start your connection with the Pushover API server
	conn = httplib.HTTPSConnection("api.pushover.net:443")

	# Send a POST request in urlencoded json
	conn.request("POST", "/1/messages.json",
	urllib.urlencode({
	"token": application_token,
	"user": user_token,
	"title": title,
	"message": message,
	"url": url,
	}), { "Content-type": "application/x-www-form-urlencoded" })

	# Listen for any error messages or other responses
	conn.getresponse()
