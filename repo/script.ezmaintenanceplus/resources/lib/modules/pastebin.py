# -*- coding: utf-8 -*-
import requests, base64

from resources.lib.modules.backtothefuture import PY2

if PY2:
    import urlparse
    urljoin = urlparse.urljoin
else:
    import urllib
    urljoin = urllib.parse.urljoin

class api:
    def __init__(self):
        self.base_link = 'https://pastebin.com'
        self.paste_link = '/api/api_post.php'
        self.apiKey = base64.b64decode('MjNkNTNhMGMyMTdlZWY2OGM5ZWE3NDY0NDIwZTMzNmU=')


    def paste(self, text):
        url = urljoin(self.base_link, self.paste_link)
        payload = {'api_dev_key': self.apiKey, 'api_option':'paste', 'api_paste_code': text}
        result = requests.post(url, data=payload, timeout=10).content
        if not PY2:
            result = result.decode('UTF-8')
        if not self.base_link in result: return "Error: " + result
        else: return result

