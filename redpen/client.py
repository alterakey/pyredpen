import urllib3
import json

http = urllib3.PoolManager()

class RedPen:
    def __init__(self, config, input_file):
        self.conf = config
        with open(input_file, "r") as f:
            self.conf["document"] = f.read()

    def set_url(url):
        self.url = url

    def validate(self):
        r = http.request('POST', self.conf.url, body=json.dumps(self.conf.config), headers={'Content-Type':'application/json'})
        return json.loads(r.data.decode('utf-8'))
