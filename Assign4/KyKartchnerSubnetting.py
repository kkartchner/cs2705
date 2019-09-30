# Subnetting
# Ky Kartchner
# 29 Sep 2019
# CS 2705

import ipaddress
import math

def main():
# Question 1:
    print("1) What is the subnet mask value for:")
    subnetPrefixToDecimal(2, 13, 5, 11, 9, 10, 4, 14, 6, 8, 12)

# Question 2:
    IPInfoBlock("132.8.150.67/22").print(2, "ip", "na ba noha vhr nc")
    print("\tNetwork Class: classless ")

# Question 3:
    IPInfoBlock("200.16.5.74/30").print(3, "ip", "na ba noha vhr")

# Question 4:
    IPInfoBlock("166.0.13.8/255.255.252.0").print(4, "ip", "na ba noha vhr")

# Question 5:
    IPInfoBlock("10.10.10.0/255.255.240.0").print(5, "subnet", "bc noha")

# Question 6:
    IPInfoBlock("10.10.10.0/255.255.255.192").print(6, "subnet", "bc noha")

# Question 7:
    IPInfoBlock("10.10.10.0/255.255.252.0").print(7, "subnet", "bc noha")

# Question 8:
    IPInfoBlock("10.10.10.0/255.255.255.248").print(8, "subnet", "bc noha")

# Question 9:
    print("\n9) You’re a manager of a network that has 56 remote site and you have",
    "one Class B license. What subnet mask would you use with having the max amount",
    "of hosts at each site 1000?")
    # Class B = subnet /16 = 11111111.11111111.00000000.00000000
    # 56 subnets <= 64 -> 2^6; borrowed bits = 6
    bitsBorrowed = 6
    prefixlen = 16 + bitsBorrowed
    mask = subnetPrefixToDecimal(prefixlen, show_message=False)
    print("\tSubnet: {}".format(mask))

    IPInfoBlock(("192.168.1.2/"+str(mask))).print(0, "", ("noha nosn"+str(bitsBorrowed)))
    

# Convert subnet prefix to decimal
def subnetPrefixToDecimal(*prefixlens, show_message=True):
    question_num = 1
    for prefix in prefixlens:
        mask = ipaddress.ip_interface('192.168.1.2/{}'.format(prefix)).netmask
        if (show_message):
            print ("\t{}. {}-bit mask: {}".format(question_num, prefix, mask))
            question_num += 1
        else:
            return mask
    
# Helper class for printing info    
class IPInfoBlock:
    def __init__(self, ip):
        self.__ip_address = ip
        self.__interface = ipaddress.ip_interface(ip)
        self.__network = self.__interface.network        

    def print (self, question_num, question_type, info_flags):
        if (not question_num == 0):
            if (question_type == 'subnet'):
                print("\n{}) Use the IP address {} and find the following:"
                    .format(question_num, self.__ip_address))
            elif (question_type == 'ip'):
                print("\n{}) With this subnet mask {} answer the following:".format(question_num, self.__interface.netmask))
            
        if ('na' in info_flags): # Print network address
            print("\tNetwork Address:", self.__network.network_address)

        if ('ba' in info_flags): # Print broadcast address
            print("\tBroadcast Address:", self.__network.broadcast_address)

        if ('noha' in info_flags): # Print number of host addresses
            print("\tNumber of Host Addresses:", len(list(self.__network.hosts())))

        if ('vhr' in info_flags): # Print valid host address range
            print("\tValid Host Address Range: {} - {}".format(self.__network.network_address+1,
             self.__network.broadcast_address-1))

        if ('bc' in info_flags): # Print valid host address range
            print("\t# of Bits used in subnet mask:", self.__network.prefixlen)
        
        if ('nosn' in info_flags):
            start = info_flags.find('nosn') + 4
            len_diff = int(info_flags[start])
            print("\tNumber of Subnets: {}".format(2**len_diff))

main()