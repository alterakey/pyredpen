import urllib2
import json
import argparse
import sys

DEFAULT_URL = "http://redpen.herokuapp.com/rest/document/validate/json"

class RedPen:
    def __init__(self, input_file, conf_file):
        self.doc = open(input_file).read()        
        self.conf = json.loads(open(conf_file).read())
        self.conf["document"] = self.doc
        self.url = DEFAULT_URL

    def set_url(url):
        self.url = url

    def validate(self):
        req = urllib2.Request(self.url, data=json.dumps(self.conf), headers={'Content-Type':'application/json'})
        return json.loads(urllib2.urlopen(req).read())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', action="store", default="sampledoc-en.txt", dest="doc_file")
    parser.add_argument('--conf', action="store", default="redpen-conf.json", dest="conf_file")
    parser.add_argument('--limit', action="store", default=1, dest="limit")
    parse_results = parser.parse_args()

    redpen = RedPen(parse_results.doc_file, parse_results.conf_file)
    result = redpen.validate()

    if parse_results.limit < len(result["errors"]):
        print "Found errors more than specified limit..."
        print len(result["errors"])
        sys.exit(1)
    else:
        print "Succeeded validation"
        sys.exit(0)

