# Title: Binary & Decimal Converter
# Author: Ky Kartchner
# Date: 14 Sep 2019
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
# Convert the provided ip_address into binary using the "repeated division-by-2" method.
########################################################################################
def decimal_to_binary(ip_address):
    octets = ip_address.split(".") # Split ip into octets
    for i in range(len(octets)): # For each octet
        decimal_value = int(octets[i])
        octet_in_binary = "" 
        for j in range(8): # repeat 8 times to get the 8 binary digits in the octet 
            octet_in_binary = str(decimal_value % 2) + octet_in_binary # add remainder to beginning of string
            decimal_value //= 2 # integer divide by 2
        octets[i] = octet_in_binary

    ip_in_binary = octets[0]
    for i in range(1, len(octets)):
        ip_in_binary += ("." + octets[i])

    print(ip_address, "converted to binary is:", ip_in_binary)


########################################################################################
# Convert the provided binary ip_address into decimal by adding the 2's place values that
# contain one.
########################################################################################
def binary_to_decimal(ip_address):
    octets = ip_address.split(".")
    for i in range(len(octets)):
        octet_decimal_value = 0
        value_to_add = 2 ** (len(octets[i]) - 1)
        for digit in octets[i]:
            if digit == '1':
                octet_decimal_value += value_to_add
            value_to_add //= 2
        octets[i] = str(octet_decimal_value)
    ip_in_decimal = octets[0]
    for i in range(1, len(octets)):
        ip_in_decimal += ("." + octets[i])

    print(ip_address, "converted to decimal is:", ip_in_decimal)

################################################################
main()
