#!/usr/bin/python 

# This file is a custom implementation of the utility functions
# provided in the official Openstack documentation, along with 
# some custom alteration. 
# Link to original source 
#   https://docs.openstack.org/user-guide/sdk-neutron-apis.html


def print_values(val, type):
    if type == 'ports':
        val_list = val['ports']

    if type == 'networks':
        val_list = val['networks']
    
    if type == 'routers':
        val_list = val['routers']

    for p in val_list:
        for k,v in p.items():
            print ("%s : %s" % (k, v))
        print ('\n')


def print_values_server(val, server_id, type):
    if type == 'ports':
        val_list = val['ports']

    if type == 'networks':
        val_list = val['networks']

    for p in val_list:
        bool = False
        for k, v in p.items():
            if k == 'device_id' and v == server_id:
                bool = True
        if bool:
            for k, v in p.items():
                print ("%s : %s" %(k, v))
            print ('\n')
