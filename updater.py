#!/usr/bin/env python3

import OpnsenseIP
import Gandi


def main(
        router_hostname, router_apikey, router_apisecret,
        gandi_apisecret, domain, iface_mapping):
    router_conn = OpnsenseIP.OpnSense(
        router_hostname, router_apikey, router_apisecret)
    router_ipdict = router_conn.GetIps()

    gandi_conn = Gandi.LiveDNS(gandi_apisecret)
    for h in iface_mapping:
        dns_ip = gandi_conn.GetARecord(domain, h)
        iface = iface_mapping[h]
        router_ip = router_ipdict[iface]

        if dns_ip != router_ip:
            print('Mismatch between gandi/%s and router/%s, updating...' % (
                dns_ip, router_ip))
            gandi_conn.SetARecord(domain, h, router_ip)
        else:
            print('Both gandi and router have %s for %s.%s.' % (
                dns_ip, h, domain))


if __name__ == '__main__':
    iface_mapping = {
        'external-name-1': 'igb0',
        'external-name-2': 'igb2'
    }
    domain = 'example.com'

    router_hostname = '192.168.1.1'
    router_apikey = 'my_router_apikey' # noqa
    router_apisecret = 'my_router_apisecret'

    gandi_apisecret = 'my_gandi_apisecret'
    main(
        router_hostname, router_apikey, router_apisecret, gandi_apisecret,
        domain, iface_mapping)
