# OpnsenseToGandi
python scripts for updating Gandi LiveDNS based on interface addresses on Opnsense

This came about as I was wanting to update multiple DNS records hosted with
Gandi LiveDNS based on multiple WAN connections on my Opnsense router.

`updater.py` should give you a pretty good idea of the intent. For your own
purposes, you can modify it, or else import it into your own module
and call the main in a similar manner as the example show in there.

If you want to call `updater.py` directly, you can simply create a
file named `config.py` with the following (be sure to modify for your use)
```
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
```

Both the `Gandi.py` and `Opnsense.py` modules are fairly standalone, which
could allow you to embrace/extend for other projects.

# Dependency
requests