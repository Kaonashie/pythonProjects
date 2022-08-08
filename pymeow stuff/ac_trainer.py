from pymeow import *

process = process_by_name("ac_client.exe") 
#print(process)
base_address = process["modules"]["ac_client.exe"]["baseaddr"] + 0x4194304
print(hex(base_address))




class Pointers:
    ammo_ptr = 0x000DDE48
    
class Offsets:
    ammo_offset = 0x34, 0x88, 0xD4, 0xF0, 0x38, 0x54, 0x140
    
    
    
    