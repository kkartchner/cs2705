# Classroom Networking Lab 
# Ky Kartchner
# 15 Oct 2019
# CS 2705

import ipaddress

############################################################################
# Subnets the main network address '138.191.0.0/25' into subnetworks of the
# following specifications:
#   CLassroom 1 - 30 computers and printers (32 addresses)
#   CLassroom 2 - 30 computers and printers (32 addresses)
#   CLassroom 3 - 14 computers (16 addresses)
#   CLassroom 4 - 14 computers (16 addresses)
#   CLassroom 5 - 14 computers (16 addresses)
#   Lab 1 - 6 computers (8 addresses)
#   Lab 2 - 6 computers (8 addresses)
#############################################################################
def main():
    main_network = ipaddress.ip_network('138.191.0.0/25') # 128 total addresses
    # Split 128-address main network into 4 32-address subnets: 128 / 32 = 4
    net32s_split = list(main_network.subnets(prefixlen_diff=2))

    # Split a 32-address subnet into 2 16-address subnets: 32 / 16 = 2
    net16s_split1 = list(net32s_split[2].subnets())

    # Split the last 32-address subnet into 2 16-address subnets: 32 / 16 = 2
    net16s_split2 = list(net32s_split[3].subnets())

    # Split the remaining 16-address subnet into 2 8-address subnets: 16 / 8 = 2
    net8s_split = list(net16s_split2[1].subnets())


    # Print networks in longest mask order:
    header_string = '\n{:-^47}\n{: ^47}'.format('-', '/{} Networks:')
    print(header_string.format('29'))
    print_network_info("Lab 1", net8s_split[0])
    print_network_info("Lab 2", net8s_split[1])

    print(header_string.format('28'))
    print_network_info("Classroom 3", net16s_split1[0])
    print_network_info("Classroom 4", net16s_split1[1])
    print_network_info("Classroom 5", net16s_split2[0])

    print(header_string.format('27'))
    print_network_info("Classroom 1", net32s_split[0])
    print_network_info("Classroom 2", net32s_split[1])

#############################################################################
# Print out network information for the specified network with specified name:
#############################################################################
def print_network_info (name, network):
    print('-----------------------------------------------')
    print('Name: ', name)
    print('Prefix Length: ', network.prefixlen)
    print('Network Address: ', network.network_address)
    print('Broadcast Address: ', network.broadcast_address)
    print('Number of Devices: ', len(list(network.hosts())))
    print('Valid Host Range: {} - {}'.format(((network.network_address)+1),((network.broadcast_address)-1)))
    # Valid Host range

main()
