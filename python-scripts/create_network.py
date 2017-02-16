#!/usr/bin/python 


from neutronclient.v2_0 import client 
from credentials import get_credentials


network_name = 'sample_network'
credentials = get_credentials()
neutron = client.Client(**credentials)

try:
    body = {'network': {'name': 'nova',
        'router:external': True,
        'provider:network_type': 'flat', 
        'provider:physical_network': 'datacenter'}}

    netw = neutron.create_network (body = body)
    net_dict = netw['network']
    network_id = net_dic['id']

    print ('Network %s created' % network_id)
finally:
    print ('Execution completed')
