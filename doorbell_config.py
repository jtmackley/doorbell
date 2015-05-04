import json
import os.path

def write(config_file,config):
	# Write our config
	print "Writing config..."
	with open(config_file, 'w') as f:
		json.dump(config, f, sort_keys=True, indent=4, separators=(',', ': '))

def read(config_file):
	# Build a default
	config= {
	"message":"Ding Dong",
	"mp3":"bell.mp3",
	"gpio_pin":2,
	"pushover_url":"",
	"pushover_app_token":"",
	"pushover_user_token":"",
	"pushover_title":"Doorbell"}
	# Check for config file
	if os.path.isfile(config_file): 
		# Open the file
		print "Reading config..."
		with open(config_file, 'r') as f:
			# Get the json
			config = json.load(f)
	else:
		print "Generating default config..."
		# Write it
		write(config_file,config)
		# read it back
		read(config_file)
	return config 
