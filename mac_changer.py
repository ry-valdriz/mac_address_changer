#!/usr/bin/env python

import subprocess
import optparse as op
import re 

def change_mac(interface, new_mac):
    # interface = "eth0"
    # new_mac = "08:00:27:5b:b1:a6" #original
    # new_mac = "00:11:22:33:44:55"

    print("[+] Changing Mac address for " + interface)
    print("[+] New MAC address: " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    #command line arguments
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface that will have its MAC address changed")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify an interface to use, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address to use, use --help for more info")

    return options

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    print(ifconfig_result)

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("current mac: ", str(current_mac))

#change MAC
change_mac(options.interface, options.new_mac) 

#check if mac was changed successfully
current_mac = get_current_mac(options.interface)
if (current_mac == options.new_mac):
    print("[+] MAC address was successfully changed")
else:
    print("[-] MAC address was not changed")



