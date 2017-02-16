#!/usr/bin/python 

# This file is a custom implementation of the information 
# provided by the Openstack documentation pages. 
# Specification https://docs.openstack.org/user-guide/sdk-neutron-apis.html


import json 
import os


def get_credentials():
    """
    This basically sets up a credentials dictionary 
    needed to be obtained from the environment variables

    @return Returns a dictionary of variables
    """
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_credentials():
    """
    This functions sets up the credentials for the 
    Nova client. 

    @return Returns a dictionary of variables
    """
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d
