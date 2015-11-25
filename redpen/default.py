import json
import os

DEFAULT_URL = "http://pyredpen-sandbox-2.herokuapp.com/rest/document/validate/json"

def data_file_named(fn):
    return os.path.join(os.path.dirname(__file__), 'data', fn)

class Config:
    def __init__(self):
        self.url = DEFAULT_URL
        self.config = {
            "format": "json2",
            "documentParser": "PLAIN",
            "config":None
        }

    def as_json(self):
        return json.dumps(self.config)

    def __getitem__(self, k):
        return self.config[k]

    def __setitem__(self, k, v):
        self.config[k] = v

    def __delitem__(self, k):
        del self.config[k]

    def update(self, d):
        self.config.update(d)

    def parser(self, parser):
        self.config['documentParser'] = parser

    def is_language_set(self):
        try:
            return 'lang' in self.config['config']
        except TypeError:
            return False

    def language(self, lang):
        if self.config['config'] is None:
            with open(data_file_named(dict(en='default-en.json', ja='default-ja.json')[lang]), 'rb') as f:
                self.config['config'] = json.loads(f.read().decode('UTF-8'))
        self.config['config']['lang'] = lang
