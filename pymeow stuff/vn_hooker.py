from pymeow import *

process = process_by_name("deaddayscrack.exe")
print(process)
base_address = process["modules"]["deaddayscrack.exe"]["baseaddr"] + 0x4194304
#print(base_address)


text_pointer = 0x0000
text_offset = 0x0000
