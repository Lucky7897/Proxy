
proxies = {'http': {}, 'socks4': {}, 'socks5': {}}

def get_proxies(protocol):
    # Return proxies by protocol
    return proxies.get(protocol, {})

def get_raw_proxies():
    # Return all raw proxies
    pass

def clean_old_proxies():
    # Clean outdated proxies
    pass
