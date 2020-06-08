#!/usr/bin/env python3

import requests
import json


class LiveDNS:
    def __init__(self, apikey):
        self.base_url = 'https://api.gandi.net/v5/livedns'
        self.apikey = apikey
        self.s = requests.Session()
        self.headers = {
            'Authorization': 'Apikey %s' % apikey,
            'Content-Type': 'application/json'
        }
        self.s.headers.update(self.headers)

    def LiveGet(self, uri):
        url = '%s/%s' % (self.base_url, uri)
        resp = self.s.get(url)
        return resp.json()

    def LivePut(self, uri, data):
        url = '%s/%s' % (self.base_url, uri)
        print(url)
        resp = requests.put(url, data=data, headers=self.headers)
        return resp.json()

    def GetARecord(self, domain, hostname):
        uri = 'domains/%s/records/%s' % (domain, hostname)
        resp = self.LiveGet(uri)
        ip = resp[0]['rrset_values'][0]
        return ip

    def SetARecord(self, domain, hostname, ip):
        data = {
            'rrset_name': hostname,
            'rrset_type': 'A',
            'rrset_values': [ip],
            'rrset_ttl': 300,
        }
        uri = 'domains/%s/records/%s/A' % (domain, hostname)
        resp = self.LivePut(uri, data=json.dumps(data))
        return resp


if __name__ == '__main__':
    api_secret = 'Get this from gandi'
    domain = 'domain-hosted-with-gandi.net'
    hostname = 'www'
    conn = LiveDNS(api_secret)
    ip = conn.GetARecord(domain, hostname)
