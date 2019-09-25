# CS 2705
# IP4 Address Manipulation
# Ky Kartchner
# 24 Sep 2019

import ipaddress
import math


class IPInfoBlock:
    def __init__(self, ip):
        self.__interface = ipaddress.ip_interface(ip)
        self.__network = ipaddress.ip_network(
            self.__interface.network) 
    
    def print(self, question_number, infoFlags):
        if (not question_number == 0):
            print('Question {}:'.format(question_number))
        if ('na' in infoFlags):
            print("Network address =", self.__network.network_address)

        if ('fua' in infoFlags):
            print("First usable address =", (self.__network.network_address + 1))

        if ('ba' in infoFlags):
            print("Broadcast address =", self.__network.broadcast_address)

        if ('lua' in infoFlags):
            print("Last usable address =", (self.__network.broadcast_address - 1))

        if ('ta' in infoFlags): #Total addresses
            print("Total addresses =", self.__network.num_addresses)

        if ('tua' in infoFlags): #Usable addresses
            print("Usable addresses =", (self.__network.num_addresses - 2))

        if ('los' in infoFlags):
            start = infoFlags.find('los') + 3
            len_diff = int(infoFlags[start])
            print("List of {} subnets =".format(2**len_diff), list(
                self.__network.subnets(prefixlen_diff=len_diff)), sep="\n  ")
        print()
        

# Question 1:
IPInfoBlock('192.168.2.76/28').print(1, 'na fua')

# Question 2:
IPInfoBlock('192.168.2.76/9').print(2, 'na fua')

# Question 3:
IPInfoBlock('192.168.2.137/27').print(3, 'na fua')

# Question 4:
IPInfoBlock('101.10.2.8/15').print(4, 'ta tua')

# Question 5:
IPInfoBlock('101.10.2.8/29').print(5, 'ta tua')

# Question 6:
IPInfoBlock('192.168.2.137/27').print(6, 'ba lua')

# Question 7:
IPInfoBlock('110.10.2.55/30').print(7, 'ba lua')

# Question 8:
extra_needed_bits = math.ceil(math.log2(10))
print('Question 8:')
print('Prefix length is the starting prefix (/20) + additional needed bits.',
    'The number of needed bits for 10 subnets is >= ceil(log2(10)) which is:',
    extra_needed_bits,"So the prefix length is /{}".format(20 + extra_needed_bits))
print()

# Question 9:
print('Question 9:')
print('To determine the max number of subnets, you can take /28 - /25, which is 3.',
      'Then raising 2 to the power of 3 you get', 2**3)
print('8 subnets with', ipaddress.ip_network('110.10.10.64/28').num_addresses,
      'addresses in each subnet.')
IPInfoBlock('110.10.10.64/25').print(0,'los3')

# Question 10:
IPInfoBlock('156.78.51.24/25').print(10, 'ta')

# Question 11:
IPInfoBlock('156.78.51.24/30').print(11, 'ta')

# Question 12:
IPInfoBlock('166.25.132.0/3').print(12, 'ta')