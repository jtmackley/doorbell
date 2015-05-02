import RPi.GPIO as GPIO
import time
import doorbell_alert as alert

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
while True:
        #take a reading
        input = GPIO.input(2)
        #if the last reading was low and this one high, print
        if ((not prev_input) and input):
		alert.alert()
		
        #update previous input
        prev_input = input
        #slight pause to debounce
        time.sleep(0.05)

