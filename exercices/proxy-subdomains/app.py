import time
import os

from flask import Flask, request
import urllib.request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info('Request received')
    o = urlparse(request.base_url)
    machine_name = o.hostname.split(".")[0].replace("-", "_")
    proxy_to_url = os.getenv(f'PROXY_TO_{machine_name}')
    app.logger.info(proxy_to_url)
    content = urllib.request.urlopen(proxy_to_url).read()
    return content