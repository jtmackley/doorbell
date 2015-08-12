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
timer=[]
timer.append(time.time())
timer.append(time.time())
processing=[]
processing.append(0)
processing.append(0)

def ButtonPressed(GPIO_BUTTON):
    if processing[0]==0:
        processing[0]=1
        if time.time()>timer[0]:
            timer[0]=time.time() + cfg["alert_timeout"]
            alert.alert(cfg,action=1)
        else:
            print "Ignoring event"
        processing[0]=0

def SensorDetect(GPIO_SENSOR):
    if processing[1]==0:
        processing[1]=1
        if time.time()>timer[1]:
            timer[1]=time.time() + cfg["alert_timeout"]
            alert.alert(cfg,action=2)
        else:
            print "Ignoring event"
        processing[1]=0

if cfg["app_debug"]:
    print "Entering Debug Mode..."
    SensorDetect(GPIO_SENSOR)
    SensorDetect(GPIO_SENSOR)
    time.sleep(30)
    SensorDetect(GPIO_SENSOR)
    time.sleep(30)
    SensorDetect(GPIO_SENSOR)


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

