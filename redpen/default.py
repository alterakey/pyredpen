DEFAULT_URL = "http://redpen.herokuapp.com/rest/document/validate/json"

class Config:
    def __init__(self):
        self.url = DEFAULT_URL
        self.config = {
            "lang": "en",
            "format": "json2",
            "documentParser": "MARKDOWN",
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

    def __getitem__(self, k):
        return self.config[k]

    def __setitem__(self, k, v):
        self.config[k] = v

    def __delitem__(self, k):
        del self.config[k]

    def update(self, d):
        self.config.update(d)
