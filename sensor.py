#!/usr/bin/python3

import time
import blynklib
BLYNK_AUTH = '2IkcFBXw1jRdFeMD0Y-3RmG2j3q-7EPJ'
blynk = blynklib.Blynk(BLYNK_AUTH)
teller=0

while True:
    teller=teller+1
    blynk.run()
    blynk.virtual_write( 12 , teller )
    print("I'm writing!")
    time.sleep(1)
