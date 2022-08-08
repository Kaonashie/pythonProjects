import pymeow
import wmi
from pymeow import *
from wmi import *


def print_proc():
    f = wmi.WMI()
    proc_name = ""
    proc_id = ""
    proc_list = []
    print("pid Process name")
    for process in f.Win32_Process():
        print(f"{process.ProcessId:<10} {process.Name}")
        #proc_name = process.Name
        #proc_id = process.ProcessId
        #proc_list += [(proc_name, proc_id)]

    #print(proc_list)

print_proc()

# process = process_by_name("ac_client.exe")
# base_address = process["modules"]["ac_client.exe"]["baseaddr"]

# print(base_address)
