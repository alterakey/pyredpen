import requests
import json

class RedPen:
    def __init__(self):
        self.doc = ""
        self.lang = "en"
        self.format = "json2"
        self.parser = "PLAIN"
        self.validators = []

    def generate(self):
        return {
            "document": "Some software tools work in more than one machine, and such distributed (cluster)systems can handle huge data or tasks, because such software tools make use of large amount of computer resources.\nIn this article, we'll call a computer server that works as a member of a cluster an \"instance\". for example, each instance in distributed search engines stores the the fractions of data.\nSuch distriubuted systems need a component to merge the preliminary results from member instnaces.",
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

class Builder:
    def __init__(self):
        self.redpen = RedPen()
        
    def add_doc(self, doc):
        self.redpen.doc = doc
    
if __name__ == '__main__':
    query = {
        "document": "Some software tools work in more than one machine, and such distributed (cluster)systems can handle huge data or tasks, because such software tools make use of large amount of computer resources.\nIn this article, we'll call a computer server that works as a member of a cluster an \"instance\". for example, each instance in distributed search engines stores the the fractions of data.\nSuch distriubuted systems need a component to merge the preliminary results from member instnaces.",
        "lang": "en",
        "format": "json2",
        "documentParser": "PLAIN",
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

    redpen = RedPen()
    r = requests.post('http://redpen.herokuapp.com/rest/document/validate/json', json=redpen.generate())
    print json.dumps(r.json(), indent=4)
