# DNS Assignment
# Ky Kartchner
# 10 Nov 2019
# CS 2705

import subprocess

###########################################################
# Look up various web addresses using dns_lookup function
###########################################################
def main():
    # Problem one
    dns_lookup("weber.edu")

    # Problem two
    dns_lookup("deseretnews.com")

    # Problem three
    dns_lookup("weber.edu", "mx")
    dns_lookup("gmail.com", "mx")

    # Problem four
    dns_lookup("yahoo.com", "ns") 
    dns_lookup("microsoft.com", "ns")

    # Problem five
    dns_lookup("www.dell.com", dns_server="8.8.8.8")
    dns_lookup("www.hp.com", dns_server="8.8.8.8")


###########################################################
# dns_lookup:
# Perform a dns lookup of the specified web address using nslookup, host, and dig 
# in succession.
#
# @param web_address: the web address to lookup
# @param lookup_type: set the type to show (ns or mx) or blank for default
# @param dns_server: dns server to use
###########################################################
def dns_lookup (web_address, lookup_type="", dns_server=""):
    lookup_types = ["mx", "ns"]
    ns_lookup_types = ["-query=mx", "-query=ns"]
    host_lookup_types = ["mx", "ns"]
    dig_lookup_types = ["MX", "NS"]

    ns_args = ["nslookup", web_address]
    host_args = ["host", web_address]
    dig_args = ["dig", web_address]

    if (lookup_type != ""):
        id = lookup_types.index(lookup_type)
        ns_args.append(ns_lookup_types[id])
        dig_args.append(dig_lookup_types[id])
        host_args.insert(1, "-t")
        host_args.insert(2, host_lookup_types[id])

    if (dns_server != ""):
        ns_args.append(dns_server)
        host_args.append(dns_server)
        dig_args.insert(1, ("@" + dns_server))

    headerStr = "\n{:-^50}"
    print(headerStr.format("Begin {} DNS Search Processes for {}", lookup_type, web_address))

    print(headerStr.format("using nslookup for " + web_address))
    subprocess.call(ns_args)

    print(headerStr.format("using host for " + web_address))
    subprocess.call(host_args)

    print(headerStr.format("using dig for " + web_address))
    subprocess.call(dig_args)

    print(headerStr.format("-"))
    print(headerStr.format("-"))

main()