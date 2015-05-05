import time
import doorbell_config as config
import doorbell_alert as alert
import sys

config_file="config.json"
cfg=config.read(config_file)

if not cfg["debug"]:
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        cfg["debug"]="True"

if cfg["debug"]:
    alert.alert(cfg)
    sys.exit("Debug End")
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cfg["gpio_pin"],GPIO.IN)

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = GPIO.input(cfg["gpio_pin"])
while True:
        #take a reading
        input = GPIO.input(cfg["gpio_pin"])
        #if the last reading was low and this one high, print
        if ((not prev_input) and input):
            alert.alert(cfg)
		
        #update previous input
        prev_input = input
        #slight pause to debounce
        time.sleep(0.05)

