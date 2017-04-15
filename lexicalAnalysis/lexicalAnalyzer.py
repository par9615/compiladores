import re

class TokenizerException(Exception): pass

class Token(object):
    def __init__(self,pattern): 
        self.token_re = re.compile(pattern, re.VERBOSE)

    def getTokens(self, text):
        return tokenizeText(text)

    def tokenizeText(self, text):
        pos = 0
        tokens = []
        while True:
            m = self.token_re.match(text, pos)
            if not m: break
            pos = m.end()
            tokname = m.lastgroup
            tokvalue = m.group(tokname)
            tokens.append((tokname, tokvalue))
        if pos != len(text):
            raise TokenizerException('tokenizer stopped at pos %r of %r with %s' % (
                pos, len(text), text))
        return tokens
