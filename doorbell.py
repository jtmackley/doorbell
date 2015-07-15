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
GPIO_BUTTON=cfg["gpio_button_pin"]
GPIO_SENSOR=cfg["gpio_sensor_pin"]
def ButtonPressed(GPIO_BUTTON):
    alert.alert(cfg,action=1)

def SensorDetect(GPIO_SENSOR):
    alert.alert(cfg,action=2)

if cfg["app_debug"]:
    print "Entering Debug Mode..."
    alert.alert(cfg,cfg["app_debug"])

if ignore_gpio:
    print "Quitting..."
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cfg["gpio_button_pin"],GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cfg["gpio_sensor_pin"],GPIO.IN)

    #initialise a previous input variable to 0 (assume button not pressed last)
    print "Waiting..."
    try:
        GPIO.add_event_detect(cfg["gpio_button_pin"], GPIO.RISING, callback=ButtonPressed)
        GPIO.add_event_detect(cfg["gpio_sensor_pin"], GPIO.RISING, callback=SensorDetect)
        while 1:
                time.sleep(100)
    except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()

