#!/usr/bin/python 

# Note that this file uses the v2_0 authentication 
# client and thus needs the file overcloudrc 
# and not the file overcloudrc.v3

from neutron_utils import authenticate_neutron
import argparse
import timeit

# start by obtaining the arguments
parser = argparse.ArgumentParser(description="Create an external network to which \
        floating IPs can be associated")
parser.add_argument("name", help="The name to be used for the created external network")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

network_name = args.name
verbose = args.verbose

start_time = timeit.default_timer()

# get the neutron client
neutron = authenticate_neutron(start_time, verbose)

# get the neutron credentials
#credentials = get_credentials()

## check for missing credentials
#for k, v in credentials.items():
#    if (v == None or v == " "):
#        msg = "Invalid credential value for key %s" % k
#        print_completion_time(start_time)
#        exit_with_error_message(msg)
#
#if verbose:
#    elapsed = timeit.default_timer() - start_time
#    print ("[@ %f] Authenticating to neutron client" % elapsed)
#
#neutron = client.Client(**credentials)
#
#if verbose:
#    elapsed = timeit.default_timer() - start_time
#    print ("[@ %f] Authentication successful" % elapsed)

try:
    body = {'network': {'name': network_name,
        'router:external': True,
        'provider:network_type': 'flat', 
        'provider:physical_network': 'datacentre'}}

    netw = neutron.create_network (body = body)
    net_dict = netw['network']
    network_id = net_dict['id']

    print ('Created Network ID is %s' % network_id)
finally:
    elapsed = timeit.default_timer() - start_time
    print_completion_time (start_time, elapsed)
