# Author: Oliquino, Alfred B.
# Subject: ETHIHAC 

#!/usr/bin/env python3

import argparse
import colorama
from colorama import Fore, Back, Style

# Check if Scapy is already installed. If not, prompt the user to install the library.
try: 
	import scapy.all as scapy
except ImportError:
	print("Scapy library is not yet installed on your system.  Run 'sudo apt-get install python3-scapy' to install  it.")
	print("Visit https://scapy.readthedocs.io/en/latest/installion.html for more information.")
	print("Always install the latest version of Scapy")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
parser.add_argument('-v', '--v', action = 'store_true', help = 'Show tool\'s version/about.')
options = parser.parse_args()
	
def scan(ip):
	arp_req_frame = scapy.ARP(pdst = ip)

	broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    
	broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

	answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
	result = []
	for i in range(0,len(answered_list)):
		client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
		result.append(client_dict)
	return result
  
def display_result(result):
	print("--------------------------------------------------------------------------------")
	print(Fore.CYAN +"Live Host\tMAC Address\t\tICMP Echo Reply\t\tOpen Ports" + Style.RESET_ALL)
	print("--------------------------------------------------------------------------------")
	for i in result:
		print("{}\t{}".format(i["ip"], i["mac"]))

if options.target:
	try:
		scanned_output = scan(options.target)
		display_result(scanned_output)
	except (KeyboardInterrupt, SystemExit):
		print("Press Ctrl+C to quit.")
elif options.v:
	print("""
	\33[33m█▀█ █▀█ █▀█ ▀█▀   █▄▀ █▄░█ █▀█ ▀▄▀ ▀▄▀
	\33[33m█▀▀ █▄█ █▀▄ ░█░   █░█ █░▀█ █▄█ █░█ █░█ (v1.2)
	""")
	print("Network Discovery Tool by Alfred Oliquino (ETHIHAC - S11)")
	print("Port Knoxx is a tool that can find live hosts and open ports using Scapy.")
	print("For the short documentation about the tool, please visit: https://bit.ly/3sOAx1H")
else:
	print("""
	\33[33m█▀█ █▀█ █▀█ ▀█▀   █▄▀ █▄░█ █▀█ ▀▄▀ ▀▄▀
	\33[33m█▀▀ █▄█ █▀▄ ░█░   █░█ █░▀█ █▄█ █░█ █░█ (v1.2)
	""")
	print(Fore.CYAN + "optional arguments:")
	print("  -h, --help                       Show this help message and exit")
	print("  -t TARGET, --target TARGET       Target IP Address/Adresses")
	print("  -v, --v                          Show tool's version/about.")
