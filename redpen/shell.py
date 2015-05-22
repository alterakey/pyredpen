import getopt
import sys

import redpen.client
import redpen.default
import redpen.flymake

def _as_bytes(f):
    try:
        return f.buffer
    except AttributeError:
        return f

def validate():
    conf = redpen.default.Config()
    url = None
    limit = None
    opts, args = getopt.getopt(sys.argv[1:], 'c:smpwejl:', ['conf', 'server', 'markdown', 'plain', 'wiki', 'english', 'japanese', 'limit'])
    for o,a in opts:
        if o in ('-c', '--conf'):
            with open(a, 'r') as f:
                conf.update(json.load(f))
        if o in ('-s', '--server'):
            url = a
        if o in ('-m', '--markdown'):
            conf.parser('MARKDOWN')
        if o in ('-p', '--plain'):
            conf.parser('PLAIN')
        if o in ('-w', '--wiki'):
            conf.parser('WIKI')
        if o in ('-e', '--english'):
            conf.language('en')
        if o in ('-j', '--japanese'):
            conf.language('ja')
        if o in ('-l', '--limit'):
            limit = int(a)

    try:
        fn = args[0]
        with open(fn, "rb") as f:
            rp = redpen.client.RedPen(conf, f.read().decode("utf-8"))
    except IndexError:
        fn = None
        rp = redpen.client.RedPen(conf, _as_bytes(sys.stdin).read().decode('utf-8'))

    if url is not None:
        rp.set_url(url)
    return rp.validate(), fn, limit

def commandline():
    results, fn, limit = validate()
    if not results['errors']:
        print("Succeeded validation")
        sys.exit(0)
    else:
        errors_found = len(results['errors'])
        if limit is None or limit >= errors_found:
            print("Found errors (%d)" % errors_found)
            sys.exit(1)
        else:
            print("Found errors more than specified limit... (%d > %d)" % (errors_found, limit))
            print(len(results["errors"]))
            sys.exit(1)

def flymake():
    results, fn, limit = validate()
    shaper = redpen.flymake.FlymakeShaper(fn, results)
    for e in shaper.shape():
        _as_bytes(sys.stdout).write((e + "\n").encode('utf-8'))
    sys.exit(shaper.code())

def sublimelinter():
    results, fn, limit = validate()
    shaper = redpen.flymake.SublimeLinterShaper(fn, results)
    for e in shaper.shape():
        _as_bytes(sys.stdout).write((e + "\n").encode('utf-8'))
    sys.exit(shaper.code())
