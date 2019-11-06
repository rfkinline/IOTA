import time               #  Date/Time functions
import RPi.GPIO as GPIO   # Imports GPIO library
GPIO.setwarnings(False)   # Otherwise you might get a GPIO warning in the beginning

# Imports the PyOTA library
from iota import Iota
from iota import Address

# Function to check the balance of an IOTA address
def iotabalance():
    gb_result = api.get_balances(address)
    balance = gb_result['balances']
    return (balance[0])

# Define some variables
powerbalance = 0
lastbalance = 0
counter = 0

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)

def light_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn light on

def light_off(pin):
    GPIO.output(pin, GPIO.LOW) # Turn light off

# URL to IOTA fullnode used when checking balance
iotaNode = "https://nodes.thetangle.org:443"

# Create an IOTA object
api = Iota(iotaNode, "")

# IOTA address that will be used for the payments
address = [Address(b'KOZBOLMIXXTNTNSS9MSLBICPHKCESOLFMSUNRAODYJYDDLUFXSKXGIIOERSJNKEXRZFEWWGVYMTQKPQJZVDQLLRFZ9')]

# Get current address balance at startup and use it as a baseline when new funds are being added.   
currentbalance = iotabalance()
lastbalance = currentbalance
# for testing purposes remove comment sign (avoids having to do the IOTA transfer)
# powerbalance = 12

# Main loop starts here
while True:

# Check every 10 seconds for new funds arrived and add them to powerbalance.
    if counter > 9:
        currentbalance = iotabalance()
        if currentbalance > lastbalance:
            powerbalance = powerbalance + (currentbalance - lastbalance)
            lastbalance = currentbalance
        counter = 0
# Manage power balance and light ON/OFF.
    if powerbalance > 0:
        light_on(channel)
        powerbalance = powerbalance - 1
    else:
        light_off(channel)
 
    # Print remaining balance
    print ("balance: "),
    print (powerbalance)

    # Increase balance check counter
    counter = counter + 1

    # wait 1 sec.
    time.sleep(1)
