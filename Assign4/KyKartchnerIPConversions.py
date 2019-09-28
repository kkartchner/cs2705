# Title: IP Conversions 
# Author: Ky Kartchner
# Date: 28 Sep 2019 
# Course: CS 2705
def main():
    # The ip address being converted is passed into the functions as an argument.
    decimal_to_binary("192.168.3.6")
    decimal_to_binary("172.168.200.253")
    decimal_to_binary("10.200.42.93")
    decimal_to_binary("21.12.198.2")

    print() # line break

    binary_to_decimal("01101100.11001100.00110000.11001100")
    binary_to_decimal("01010110.10100011.11001111.11111111")
    binary_to_decimal("00001001.10101010.11111110.11100011")
    binary_to_decimal("10101010.01101100.11111100.01110011")


########################################################################################
# Convert the provided ip_address into binary using the built-in conversion function.
########################################################################################
def decimal_to_binary(ip_address):
    octets = ip_address.split(".") # Split ip address into octets using '.' as deliminator
    for i in range(len(octets)): # Replace each decimal octet with its binary representation 
        octets[i] = bin(int(octets[i])) [2:].zfill(8) # Remove the '0b' from each number and pad with 0s as needed

    ip_in_binary = "{0}.{1}.{2}.{3}".format(*octets) # Format binary octets as ip address
    print ("{0} converted to binary is {1}".format(ip_address, ip_in_binary))


########################################################################################
# Convert the provided ip_address into decimal using the built-in conversion function.
########################################################################################
def binary_to_decimal(ip_address):
    octets = ip_address.split(".") # Split ip address into octets using '.' as deliminator
    for i in range(len(octets)): # Convert each octet to decimal equivalent
        octets[i] = int(octets[i], 2)

    ip_in_decimal = "{0}.{1}.{2}.{3}".format(*octets) # Format decimal octets as ip address
    print ("{0} converted to decimal is {1}".format(ip_address, ip_in_decimal))


################################################################
main()
