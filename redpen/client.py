import urllib3
import json

http = urllib3.PoolManager()

class Guesser:
    def __init__(self, doc):
        self.doc = doc

    def guess(self):
        try:
            self.doc.encode('ascii')
            return "en"
        except (UnicodeEncodeError, UnicodeDecodeError):
            return "ja"

class RedPen:
    def __init__(self, config, input_file):
        self.conf = config
        with open(input_file, "rb") as f:
            doc = f.read().decode('utf-8')
            self.conf["document"] = doc
            if not self.conf.is_language_set():
                self.conf.language(Guesser(doc).guess())

    def url(self, url):
        self.url = url
        return self

    def validate(self):
        r = http.request('POST', self.conf.url, body=json.dumps(self.conf.config), headers={'Content-Type':'application/json'})
        return json.loads(r.data.decode('utf-8'))
