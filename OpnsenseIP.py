#!/usr/bin/env python3

import requests
import ipaddress
import re

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class OpnSense:
    def __init__(self, hostname, apikey, apisecret):
        self.auth = (apikey, apisecret)
        self.base_url = 'https://%s/api' % hostname

    def Get(self, uri, json_output=True):
        url = '%s/%s' % (self.base_url, uri)
        resp = requests.get(url, verify=False, auth=self.auth)
        if resp.status_code != 200:
            print('Connection issue')
            return None

        if json_output is False:
            return resp.text
        else:
            return resp.json()

    def GetIps(self):
        ipdict = {}
        uri = 'diagnostics/interface/getInterfaceStatistics'
        resp = self.Get(uri)

        for i in resp['statistics']:
            iface_info, address = i.split(' / ')
            iface = re.findall(r'\((.*?)\)', iface_info)
            if len(iface) == 0:
                iface = ''
            else:
                iface = iface[0]

            try:
                ipaddress.IPv4Address(address)
                ipdict[iface] = address
            except ipaddress.AddressValueError:
                continue
        return ipdict


if __name__ == '__main__':
    apikey = 'you need to get your own key from the router'
    apisecret = 'you need to get this too'
    conn = OpnSense('192.168.1.1', apikey, apisecret)
    ipdict = conn.GetIps()
