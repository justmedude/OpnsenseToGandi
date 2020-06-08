# OpnsenseToGandi
python scripts for updating Gandi LiveDNS based on interface addresses on Opnsense

This came about as I was wanting to update multiple DNS records hosted with
Gandi LiveDNS based on multiple WAN connections on my Opnsense router.

`updater.py` should give you a pretty good idea of the intent. For your own
purposes, you can modify it, or else import it into your own module
and call the main in a similar manner as the example show in there.

If you want to call `updater.py` directly, you just need to modify `config.py`
for your own needs.

Both the `Gandi.py` and `Opnsense.py` modules are fairly standalone, which
could allow you to embrace/extend for other projects.

# Dependency
requests