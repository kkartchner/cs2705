# Python Pinging for Fun and Profit 
# Ky Kartchner
# 3 Nov 2019
# CS 2705

import os
import subprocess

# If computer is using windows, use '-n 4' else use '-c 4'
command = '-n 4' if (os.name == 'nt') else "-c 4" 

def main():
    print(command)
    pingAddress("www.microsoft.com")
    pingAddress("www.weber.edu")
    pingAddress("www.yahoo.com")
    pingAddress("www.nhl.com")
    pingAddress("www.ksl.com")


def pingAddress(address): # Ping specified address
    print('{:-^50}\nPinging {} ...'.format('', address))
    subprocess.call(["ping", command, address])
    print()

main()
