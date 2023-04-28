import random
import json
import os

def loadProxies():
    if os.path.isfile("proxies.json"):
        f = open('proxies.json')
        data = json.load(f)
        f.close()
        return data

    return []


PROXIES = loadProxies()

proxy = False

if len(PROXIES) > 0:
    proxy = random.choice(PROXIES)