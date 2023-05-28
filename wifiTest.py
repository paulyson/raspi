

import  RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)

GPIO.output(25,GPIO.HIGH)
time.sleep(2)
GPIO.output(25,GPIO.LOW)

while True:
    try:
        response = requests.get("http://www.google.com", timeout=1)
        if response:
            for i in range(3000):
                GPIO.output(25, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(25, GPIO.LOW)
                time.sleep(0.1)
    except requests.ConnectionError:
        print("Could not connect to Google.com")
        time.sleep(600)