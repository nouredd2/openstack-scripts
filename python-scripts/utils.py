#!/usr/bin/python 

# This file is a custom implementation of the utility functions
# provided in the official Openstack documentation, along with 
# some custom alteration. 
# Link to original source 
#   https://docs.openstack.org/user-guide/sdk-neutron-apis.html

import timeit

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


def exit_with_error_message (msg):
    """
    Exit the program early and display an error message
    """
    print ("[ERROR] %s\n" % msg)
    raise SystemExit

def print_completion_time (start_time, elapsed = -1.0):
    """
    Print the completion time message. 
    If elapsed is -1.0, then compute the elapsed time from 
    the provided start time.
    """

    if (elapsed == -1.0):
        elapsed = timeit.default_timer() - start_time

    print ('Execution completed in %d seconds' % elapsed)
