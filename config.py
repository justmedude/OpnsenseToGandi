#!/usr/bin/env python3

# configs talking to opnsense host
router_hostname = '192.168.1.1'
router_apikey = '<generate this on your opnsense host>'
router_apisecret = '<generate this on your opnsense host>'

gandi_apisecret = '<my_gandi_apisecret>'

iface_mapping = {
    'external-name-1': 'igb0',
    'external-name-2': 'igb2'
}
domain = 'example.com'
