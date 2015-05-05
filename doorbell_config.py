import json
import os.path

def write(config_file,config):
	# Write our config
	print "Writing config..."
	with open(config_file, 'w') as f:
		json.dump(config, f, sort_keys=True, indent=4, separators=(',', ': '))

def read(config_file):
	# Check for config file
	if os.path.isfile(config_file): 
		# Open the file
		print "Reading config..."
		with open(config_file, 'r') as f:
			# Get the json
			config = json.load(f)
	config=check(config_file,config)
	return config 

def check(config_file,config):
	# Build a default
	default={
	"debug": 0,
	"message":"Ding Dong",
	"localsound":1,
	"mp3":"bell.mp3",
	"gpio_pin":2,
	"pushover":0,
	"pushover_title":"Doorbell",
	"pushover_user_token":"",
	"pushover_app_token":"",
	"pushover_url":""}

	writenew=False
	# Loop through our default config entries
	for defaultkey in default:
		found=False
		if not defaultkey in config:
			# Key missing - add to dict
			print "Adding new key " + defaultkey
			config[defaultkey]=default[defaultkey]
			writenew=True
		
	if writenew:
		# Write it
		write(config_file,config)

	return config