DEFAULT_URL = "http://redpen.herokuapp.com/rest/document/validate/json"

class Config:
    def __init__(self):
        self.url = DEFAULT_URL
        self.config = {
            "format": "json2",
            "documentParser": "PLAIN",
        }

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
        return 'lang' in self.config

    def language(self, lang):
        if lang == 'en':
            self.config.update({
                "lang": "en",
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
            })
        elif lang == 'ja':
            self.config.update({
                "lang": "ja",
                "config": {
                    "CommaNumber": {},
                    "DoubledWord": {},
                    "HankakuKana": {},
                    "InvalidSymbol": {},
                    "KatakanaEndHyphen": {},
                    "KatakanaSpellCheck": {},
                    "ParagraphNumber": {},
                    "SectionLength": {
                        "properties": {
                            "max_num": "1500"
                        }
                    },
                    "SentenceLength": {
                        "properties": {
                            "max_len": "100"
                        }
                    },
                    "SpaceBetweenAlphabeticalWord": {},
                    "SuccessiveWord": {}
                }
            })
