#!/usr/bin/env python

import subprocess
import optparse as op

def change_mac(interface, new_mac):
    # interface = "eth0"
    # new_mac = "08:00:27:5b:b1:a6" #original
    # new_mac = "00:11:22:33:44:55"

    print("[+] Changing Mac address for " + interface)
    print("[+] New MAC address: " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def terminal_input():
    #command line arguments
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface that will have its MAC address changed")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
    return parser.parse_args()

(options, arguments) = terminal_input()

change_mac(options.interface, options.new_mac)



