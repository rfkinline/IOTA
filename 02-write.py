#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
import SimpleMFRC522

try:
    while True:
        text = input('Your Name: ')
        print("Now place tag next to scanner to write")
        id, text = reader.write(text) 
        print("recorded")
        
        print(id)
        print(text)
finally:
    print("cleaning up")
GPIO.cleanup()
