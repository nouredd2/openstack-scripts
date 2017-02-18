#!/usr/bin/python 

# Note that this file uses the v2_0 authentication 
# client and thus needs the file overcloudrc 
# and not the file overcloudrc.v3

from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_completion_time, exit_with_error_message
import timeit

def authenticate_neutron(start_time, verbose):
    """
    Authenticate to the neutron client and 
    return the client if successful
    
    @param start_time The starting time for the verbosity prints
    @param verbose    The verbosity level

    @return Returns the neutron client if successful authentication
    """
    # get the neutron credentials
    credentials = get_credentials()

    # check for missing credentials
    for k, v in credentials.items():
        if (v == None or v == " "):
            msg = "Invalid credential value for key %s" % k
            print_completion_time(start_time)
            exit_with_error_message(msg)

    if verbose:
        elapsed = timeit.default_timer() - start_time
        print ("[@ %f] Authenticating to neutron client" % elapsed)

    try:
        neutron = client.Client(**credentials)
    except:
        elapsed = timeit.default_timer() - start_time
        print ("[@ %f] Authentication failed" % elapsed)

    if verbose:
        elapsed = timeit.default_timer() - start_time
        print("[@ %f] Authentication successful" % elapsed)

    return neutron
