import getopt
import sys

import redpen.client
import redpen.default
import redpen.flymake

def validate():
    conf = redpen.default.Config()
    limit = None
    opts, args = getopt.getopt(sys.argv[1:], 'c:l:', ['conf', 'limit'])
    for o,a in opts:
        if o in ('-c', '--conf'):
            with open(a, 'r') as f:
                conf.update(json.load(f))
        if o in ('-l', '--limit'):
            limit = int(a)

    return redpen.client.RedPen(conf, args[0]).validate(), args[0], limit

def commandline():
    result, fn, limit = validate()
    if not result['errors']:
        print("Succeeded validation")
        sys.exit(0)
    else:
        errors_found = len(result['errors'])
        if limit is None or limit >= errors_found:
            print("Found errors (%d)" % errors_found)
            sys.exit(1)
        else:
            print("Found errors more than specified limit... (%d > %d)" % (errors_found, limit))
            print(len(result["errors"]))
            sys.exit(1)

def flymake():
    results, fn, limit = validate()
    shaper = redpen.flymake.FlymakeShaper(fn, results)
    for e in shaper.shape():
        sys.stdout.buffer.write((e + "\n").encode('utf-8'))
    sys.exit(shaper.code())