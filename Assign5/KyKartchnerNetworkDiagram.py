# Network Diagram Lab
# Ky Kartchner
# 6 Oct 2019
# CS 2705

import ipaddress
import math


def main():
    main_interface = ipaddress.ip_interface('138.191.0.0/16')
    main_network = main_interface.network
    group_names = ['Applied Science', 'Arts & Humanities', 'Education', 'Business & Economics', 'Health', 'Science',
                   'Social and Behavioral Science', 'Information Technology',
                   'Student Services', 'Academic Support', 'Administrative Services']

    sub_networks = print_network_grouping("College and Departments", group_names, main_network)

    sub_departments = [['Computer Science', 'Professional Sales', 'Manufacturing Engineering', 'Construction Management', 'Automotive Technology', 'Network Technology', 'Web Design', 'Engineering'],
                       ['Korean', 'German', 'Spanish', 'French', 'English', 'Visual Arts', 'Performing Arts', 'Communications'],
                       ['Child and Family Studies', 'Health Promotion', 'Athletic Training', 'Human Performance', 'Teacher Education', 'Exercise Physiology', 'Health Education', 'Recreation Management'],
                       ['Business Administration', 'Economics', 'Information Systems Tech', 'Master of Business Admin', 'Accounting', 'Business Education', 'Master of Accountancy', 'Master of Taxation'],
                       ['Dental Hygiene', 'Emergency Care', 'Health Information Mgmt', 'Nursing', 'Medical Laboratory', 'Radiology', 'Respiratory Therapy', 'Occupational Therapy'],
                       ['Botany', 'Geosciences', 'Microbiology', 'Developmental Math', 'Physics', 'Zoology', 'Mathematics', 'Human Anatomy Physiology'],
                       ['Criminal Justice', 'Geography', 'History', 'Military Science', 'Philosophy & Poli Sci', 'Psychology', 'Social Work', 'Sociology & Anthropology'],
                       ['Computing Support', 'Telecommunications', 'Administrative Computing', 'Networking', 'Academic Computing', 'Computer Security', 'Database Administration', 'VP of IT Office'],
                       ['Student Life', 'Student Services', 'Outreach', 'Academic Support', 'Focused Interest', 'Career Services', 'Veterans Affairs', 'Diversity'],
                       ['Campus Planning', 'Construction', 'Custodial', 'Landscaping', 'Electrical', 'Mechanical', 'Business Services', 'Parking Services'],
                       ['Athletics', 'Accounting', 'Budget', 'Enviro Health & Safety', 'Printing', 'Human Resources', 'Purchasing', 'Police and Security']]

    for i in range(len(group_names)):
        print_network_grouping(group_names[i], sub_departments[i], sub_networks[i])



def print_network_grouping(header, group_names, group_network):
    print('{:-^100}'.format(header))
    format_string = "{:<35} {:<30} {}"
    print(format_string.format('Name', 'Network Address and Subnet',
                               'Subnet Host IP address range'))
    print('{:-^100}'.format(''))

    prefixlen = math.ceil(math.log2(len(group_names)))
    sub_networks = list(ipaddress.ip_network(
        group_network).subnets(prefixlen_diff=prefixlen))

    for i in range(len(group_names)):
        print(format_string.format(group_names[i], str(sub_networks[i]),
                                   '{} - {}'.format((sub_networks[i].network_address + 1), (sub_networks[i].broadcast_address - 1))))
    print()
    return sub_networks


main()
