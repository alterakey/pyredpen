import getopt
import unicodedata

class FlymakeShaper:
    def __init__(self, fn, result):
        self.fn = fn
        self.result = result

    def code(self):
        return 0

    def shape(self):
        try:
            for e in self.disassembled(self.result['errors']):
                yield '%s:%d:%d: warning: %s [%s]' % (self.fn,e['position']['start']['line'],1+e['position']['start']['offset'],e['message'],e['validator'])
        except KeyError:
            pass

    def disassembled(self, v):
        for e in v:
            try:
                for i in self.disassembled(v=e['errors']):
                    yield i
            except KeyError:
                yield e
