#!/usr/bin/env python

import subprocess

# interface = "eth0"
# original_mac = "08:00:27:5b:b1:a6"
# new_mac = "00:11:22:33:44:55"

interface = input("interface: ")
new_mac = input("new mac(xx:xx:xx:xx:xx:xx): ")

print("[+] Changing Mac address for " + interface)
print("[+] new MAC address: " + new_mac)

# subprocess.call("ifconfig eth0 down", shell = True)
# subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell = True)
# subprocess.call("ifconfig eth0 up", shell = True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
