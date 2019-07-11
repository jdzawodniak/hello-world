import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

while True:
        GPIO.output(27,GPIO.HIGH)
        print("LED is ON")
        time.sleep(3)

        GPIO.output(27,GPIO.LOW)
        print("LED is OFF")
        print ("cool")
        time.sleep(3)
