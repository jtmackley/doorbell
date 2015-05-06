print "Raspberry Pi Doorbell v0.1.000"
import time
import sys
ignore_gpio=False
try:
    import RPi.GPIO as GPIO
except ImportError:
    print "Requires RPi.GPIO"
    ignore_gpio=True
import doorbell_config as config
import doorbell_alert as alert

config_file="config.json"
cfg=config.read(config_file)


if cfg["app_debug"]:
    print "Entering Debug Mode..."
    alert.alert(cfg)

if ignore_gpio:
    print "Quitting..."
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cfg["gpio_pin"],GPIO.IN)

    #initialise a previous input variable to 0 (assume button not pressed last)
    prev_input = GPIO.input(cfg["gpio_pin"])
    print "Waiting..."
    while True:
            #take a reading
            input = GPIO.input(cfg["gpio_pin"])
            #if the last reading was low and this one high, print
            if ((not prev_input) and input):
                alert.alert(cfg)
                print "Waiting..."
    		
            #update previous input
            prev_input = input
            #slight pause to debounce
            time.sleep(0.05)

