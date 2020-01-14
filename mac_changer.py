#!/usr/bin/env python

import subprocess
import optparse as op

#command line arguments
parser = op.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "Interface that will have its MAC address changed")
parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

# interface = "eth0"
# new_mac = "08:00:27:5b:b1:a6" #original
# new_mac = "00:11:22:33:44:55"

#select interface and new mac address
#interface = input("interface: ")
#new_mac = input("new mac(xx:xx:xx:xx:xx:xx): ")

print("[+] Changing Mac address for " + interface)
print("[+] New MAC address: " + new_mac)

# subprocess.call("ifconfig eth0 down", shell = True)
# subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell = True)
# subprocess.call("ifconfig eth0 up", shell = True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
