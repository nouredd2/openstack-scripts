#!/usr/bin/python 

# Note that this file uses the v2_0 authentication 
# client and thus needs the file overcloudrc 
# and not the file overcloudrc.v3


from neutronclient.v2_0 import client 
from credentials import get_credentials


network_name = 'sample_network'
credentials = get_credentials()
neutron = client.Client(**credentials)

try:
    body = {'network': {'name': network_name,
        'router:external': True,
        'provider:network_type': 'flat', 
        'provider:physical_network': 'datacentre'}}

    netw = neutron.create_network (body = body)
    net_dict = netw['network']
    network_id = net_dict['id']

    print ('Network %s created' % network_id)
finally:
    print ('Execution completed')
