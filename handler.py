#!/usr/bin/python3

import time
import blynklib
BLYNK_AUTH = '2IkcFBXw1jRdFeMD0Y-3RmG2j3q-7EPJ'
blynk = blynklib.Blynk(BLYNK_AUTH)
criticalValue = 5

@blynk.handle_event( 'connect' )
def connect_handler():
    blynk.virtual_sync( 12 )

@blynk.handle_event( 'write V12' )
def write_handler( pin , value ):
    print( "Test" )
    print(value[0])
    if int(value[0]) >= criticalValue:
        print("Voorwaarde ok")
        blynk.set_property( 12 , 'color' , '#FF0000' ) # Rood maken
    else:
        blynk.set_property(12, 'color', '#00FF00')
    blynk.virtual_sync( 12 )
    
while True:
    blynk.run()
