import time
import os

from flask import Flask
import urllib.request

app = Flask(__name__)

proxy_to_url = os.getenv('PROXY_TO_URL')
print('PROXY_TO_URL: ' + proxy_to_url)

@app.route('/')
def hello():
    print('Request received')
    content = urllib.request.urlopen(proxy_to_url).read()
    return content