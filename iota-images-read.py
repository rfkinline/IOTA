from iota import Iota
from iota import Transaction

import json
import pprint
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Q", "Z"]

api = Iota('https://nodes.thetangle.org:443') 

# Change 1: IOTA address. Use your IOTA address
address = 'XUHJLCCEJSNGQNYHVEGDRCZWXDBZTZMFCSURNCB99XBVRRXSGIBQJDPYRUJVMIMZVTRXKYHWRVLSMTJYZCQAPYISXD'

transactions = api.find_transactions(addresses=[address,])

hashes = []
for txhash in transactions['hashes']:
    hashes.append(txhash)


trytes = api.get_trytes(hashes)['trytes']

for trytestring in trytes:

    tx = Transaction.from_tryte_string(trytestring)
# Change 2: Below is an example of a TAGg. Replace it with your own:
    if tx.tag == 'IMAGEWER9999999999999999999':
     txn_data = str(tx.signature_message_fragment.decode())
     json_data = json.loads(txn_data)
     if all(key in json.dumps(json_data) for key in ["Z","Q"]):
      x.add_row([json_data['Q'], json_data['Z']])

# Sort table 
     x.sortby = "Z"
# Don't print a broder
     x.border = False

# Print column Q to terminal
print x.get_string(fields=["Q"])
