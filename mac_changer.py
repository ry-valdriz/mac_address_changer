#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:55"

print("[+] Changing Mac address for " + interface)
print("[+] new MAC address: " + new_mac)

subprocess.call("ifconfig eth0 down", shell = True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell = True)
subprocess.call("ifconfig eth0 up", shell = True)
