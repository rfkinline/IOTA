# Original program by https://gist.github.com/huggre

# Import libraries
from datetime import datetime
import json
import iota
import RPi.GPIO as GPIO
import SimpleMFRC522

# IOTA address
CleaningLogAddr = b"XUHJLCCEJSNGQNYHVEGDRCZWXDBZTZMFCSURNCB99XBVRRXSGIBQJDPYRUJVMIMZVTRXKYHWRVLSMTJYZCQAPYISXD"

# IOTA full node
api = iota.Iota("https://nodes.thetangle.org:443")

products = "Widget ensembly"
reader = SimpleMFRC522.SimpleMFRC522()

try:
    while True:
        print("\nIOTA ensembled products")
        print("Press Ctrl+C to exit the system")
        ensembled_products = input("\nNumber of ensembled products: ")
        print("\nThank you, now hold your ID card near the reader")       
        
        id, text = reader.read()
        data = {'tagID': str(id), 'product': products, 'ensembled_products': ensembled_products}
        
        pt = iota.ProposedTransaction(address = iota.Address(CleaningLogAddr),
                                      message = iota.TryteString.from_unicode(json.dumps(data)),
                                      tag     = iota.Tag(b'WIDGETENSEMBLY'),
                                      value   = 0)

        print("\nID card detected...Sending transaction...Please wait...")

        FinalBundle = api.send_transfer(depth=3, transfers=[pt], min_weight_magnitude=14)['bundle']
    
        print("\nTransaction sucessfully recorded")
                
except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()
