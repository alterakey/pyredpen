import getopt
import unicodedata

class Guesser:
    def __init__(self, doc):
        self.doc = doc

    def guess(self):
        try:
            self.doc.encode('ascii')
            return "en"
        except UnicodeEncodeError:
            return "ja"

class FlyPen:
    def __init__(self, input_file, conf_file, api=None):
        self.doc = open(input_file).read().decode('utf-8')
        self.conf = json.loads(open(conf_file).read())
        self.conf["document"] = self.doc.encode('utf-8')
        self.conf["lang"] = Guesser(self.doc).guess()
        self.url = DEFAULT_URL

    def validate(self):
        req = urllib2.Request(self.url, data=json.dumps(self.conf), headers={'Content-Type':'application/json'})
        return json.loads(urllib2.urlopen(req).read())


class FlymakeShaper:
    def __init__(self, fn, result):
        self.fn = fn
        self.result = result

    def code(self):
        return 0

    def shape(self):
        try:
            for e in self.disassembled(self.result['errors']):
                yield '%s:%d:%d: warning: %s [%s]' % (self.fn,e['position']['start']['line'],e['position']['start']['offset'],e['message'],e['validator'])
        except KeyError:
            pass

    def disassembled(self, v):
        for e in v:
            try:
                for i in self.disassembled(v=e['errors']):
                    yield i
            except KeyError:
                yield e

def shell():
    opts,args = getopt.getopt(sys.argv[1:], 'c:', ['--conf'])
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', action="store", dest="doc_file")
    parser.add_argument('--conf', action="store", default="redpen-conf.json", dest="conf_file")
    parse_results = parser.parse_args()

    shaper = FlymakeShaper(parse_results.doc_file, FlyPen(parse_results.doc_file, parse_results.conf_file).validate())
    for e in shaper.shape():
        print e

    return shaper.code()
