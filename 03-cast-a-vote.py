# Original program by https://gist.github.com/huggre

# Import libraries
from datetime import datetime
import json
import iota
import sys
import RPi.GPIO as GPIO
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

# IOTA address
IOTAAddr = b"XUHJLCCEJSNGQNYHVEGDRCZWXDBZTZMFCSURNCB99XBVRRXSGIBQJDPYRUJVMIMZVTRXKYHWRVLSMTJYZCQAPYISXD"

# IOTA full node
api = iota.Iota("https://nodes.thetangle.org:443")

project = "Voting via RFID"
reader = SimpleMFRC522()

try:
    while True:
        print("\nIOTA Project Voting")
        
# only yes or no allowed
        while True:
           casted_vote = raw_input("\nCast your vote (YES/NO) and hit Enter: ").lower()
           if casted_vote == "yes":
               print("You voted YES")
               break
           elif casted_vote == "no":
               print("You voted NO")
               break   
        
        print("\nThank you, now hold your ID card near the reader")       
        
        id, text = reader.read()
        data = {'tagID': str(id), 'tagText':str(text), 'project': project, 'casted_vote': casted_vote}
        
        pt = iota.ProposedTransaction(address = iota.Address(IOTAAddr),
                                      message = iota.TryteString.from_unicode(json.dumps(data)),
                                      tag     = iota.Tag(b'VOTERFIDMIAMI'),
                                      value   = 0)

        print("\nID card detected...Sending transaction...Please wait...")

        FinalBundle = api.send_transfer(depth=3, transfers=[pt], min_weight_magnitude=14)['bundle']
    
        print("\nTransaction sucessfully recorded")
        break
                
finally:
    GPIO.cleanup()

