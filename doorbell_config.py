import json
import os.path

def write(config_file,config):
	# Write our config
	print "Writing config..."
	with open(config_file, 'w') as f:
		json.dump(config, f, sort_keys=True, indent=4, separators=(',', ': '))

def read(config_file):
	# Check for config file
	config={}
	if os.path.isfile(config_file): 
		# Open the file
		print "Reading config..."
		with open(config_file, 'r') as f:
			# Get the json
			config = json.load(f)
	config=check(config_file,config)
	# Fix paths
	if config["camera_local_file_path"][-1]!="/":
		config["camera_local_file_path"]+="/"
	return config 

def check(config_file,config):
	# Build a default
	default={
	"app_debug": 0,
	"app_message":"Ding Dong",
	"mp3":1,
	"mp3file":"bell.mp3",
	"gpio_button_pin":2,
	"gpio_sensor_pin":7,
	"camera":1,
	"camera_local_file_path":"/tmp",
	"ftp":0,
	"ftp_server":"",
	"ftp_user":"",
	"ftp_password":"",
	"ftp_remote_path":"doorbell",
	"mysql":0,
	"mysql_server":"",
	"mysql_user":"",
	"mysql_password":"",
	"mysql_database":"",
	"mysql_doorbell_id":"1",
	"pushbullet":0,
	"pushbullet_app_token":"",
	"pushover":0,
	"pushover_title":"Doorbell",
	"pushover_user_token":"",
	"pushover_app_token":"",
	"pushover_url":"",
	"email":0,
	"email_to":"",
	"email_subject":"",
	"email_account_user":"",
	"email_account_password":"",
	"email_server":"",
	"email_port":587,
	"email_tls":1,
	"alert_timeout":60
	"threshold": 10,
	"sensitivity": 200,
	"nightShut": 5.5
	}

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