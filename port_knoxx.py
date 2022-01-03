# Author: Oliquino, Alfred B.
# Subject: ETHIHAC

#!/usr/bin/env python3

import argparse, time, logging, sys
from threading import Thread

# Check if Scapy is already installed. If not, prompt the user to install the library.
try:
from scapy.all import *
except ImportError:
print("Scapy library is not yet installed on your system.  Run 'sudo apt-get install python3-scapy' to install  it.")
print("Visit https://scapy.readthedocs.io/en/latest/installion.html for more information.")
print("Always install the latest version of Scapy")

start = time.time()

#Argparsing
parser = argparse.ArgumentParser(description = "")

NDTO = parser.add_argument_group('Network Discovery Tool Options')
NDTO.add_argument("-p", "--p", action = "store_true", help = "Perform a scan to the target host/s. To perform a scan, run 'python3 port_knoxx.py -p [host/s]")
NDTO.add_argument("-v", "--v", action = "store_true", help = "Show tool's version/about.")

args = parser.parse_args()

#Features:
#Version (-v / --v) shows the version and about message of the tool.
if args.v:
print("""
█▀█ █▀█ █▀█ ▀█▀   █▄▀ █▄░█ █▀█ ▀▄▀ ▀▄▀
█▀▀ █▄█ █▀▄ ░█░   █░█ █░▀█ █▄█ █░█ █░█ (v1.1)
""")
print("Network Discovery Tool by Alfred Oliquino (ETHIHAC - S11)")
print("Port Knoxx is a tool that can find live hosts and open ports using Scapy.")
print("For the short documentation about the tool, please visit: https://bit.ly/3sOAx1H")
#
if args.p:
print("Scanning function here")
