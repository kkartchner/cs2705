# Title: Binary & Decimal Converter
# Author: Ky Kartchner
# Date: 15 Sep 2019
# Course: CS 2705
def main():
    decimal_to_binary("192.168.16.13")
    decimal_to_binary("64.10.241.2")
    decimal_to_binary("0.244.116.15")
    decimal_to_binary("5.255.200.153")
    decimal_to_binary("72.99.62.9")
    binary_to_decimal("10110100.11101011.00001000.10010001")
    binary_to_decimal("10001100.11111111.11000000.00000001")
    binary_to_decimal("00010001.11001100.00000001.00010010")
    binary_to_decimal("11100111.00110011.10101010.11111110")
    binary_to_decimal("00010111.11101110.01010101.10000000")

########################################################################################
# Convert the provided ip_address into binary using the built-in conversion function.
########################################################################################
def decimal_to_binary(ip_address):
    octets = ip_address.split(".")
    for i in range(len(octets)): # Replace each decimal octet with its binary representation 
        octets[i] = bin(int(octets[i])) [2:].zfill(8) # Remove the '0b' from each number and pad with 0s as needed

    ip_in_binary = "{0}.{1}.{2}.{3}".format(*octets)
    print ("{0} converted to binary is {1}".format(ip_address, ip_in_binary))


########################################################################################
# Convert the provided ip_address into decimal using the built-in conversion function.
########################################################################################
def binary_to_decimal(ip_address):
    octets = ip_address.split(".")
    for i in range(len(octets)):
        octets[i] = int(octets[i], 2)

    ip_in_decimal = "{0}.{1}.{2}.{3}".format(*octets)
    print ("{0} converted to decimal is {1}".format(ip_address, ip_in_decimal))


################################################################
main()
