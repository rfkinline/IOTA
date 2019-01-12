#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
print("Place a tag next to the reader")
try:
  id, text = reader.read()
  print(id)
  print(text)
finally:
  GPIO.cleanup()
