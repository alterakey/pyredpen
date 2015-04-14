import requests
import json
import argparse
import sys

class RedPen:
    def __init__(self):
        self.doc = ""
        self.lang = "en"
        self.format = "json2"
        self.parser = "PLAIN"
        self.validators = []
        self.url= "http://redpen.herokuapp.com/rest/document/validate/json"

    def generate(self):
        return {
            "document": self.doc,
            "lang": self.lang,
            "format": self.format,
            "documentParser": self.parser,
            "config": {
                "CommaNumber": {},
                "Contraction": {},
                "DoubledWord": {},
                "EndOfSentence": {},
                "InvalidExpression": {},
                "InvalidSymbol": {},
                "InvalidWord": {},
                "ParagraphNumber": {},
                "Quotation": {},
                "SectionLength": {
                    "properties": {
                        "max_char_num": "2000"
                    }
            },
            "SentenceLength": {
                "properties": {
                    "max_len": "200"
                }
            },
            "SpaceBetweenAlphabeticalWord": {},
                "Spelling": {},
                "StartWithCapitalLetter": {},
                "SuccessiveWord": {},
                "SymbolWithSpace": {},
                "WordNumber": {}
            }
        }

    def validate(self):
        return requests.post('http://redpen.herokuapp.com/rest/document/validate/json', json=self.generate()).json()

class Builder:
    def __init__(self):
        self.redpen = RedPen()
        
    def add_doc(self, doc):
        self.redpen.doc = doc
        return self

    def set_url(self, url):
        self.url = url
        return self

    def build(self):
        return self.redpen
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', action="store", default="sampledoc-en.txt", dest="doc_file")
    parser.add_argument('--limit', action="store", default=1, dest="limit")
    parse_results = parser.parse_args()

    redpen = Builder().add_doc(open(parse_results.doc_file).read()).build()
    result = redpen.validate()
    if parse_results.limit < len(result["errors"]):
        print "Found errors more than specified limit..."
        print len(result["errors"])
        sys.exit(1)
    else:
        print "Succeeded validation"
        sys.exit(0)

    # print json.dumps(result, indent=4)
