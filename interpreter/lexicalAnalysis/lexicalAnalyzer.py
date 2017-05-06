import re

grammarPattern = r"""
(?P<drone>drone)
|(?P<leftCurly>[{])
|(?P<rightCurly>[}])
|(?P<leftBracket>[(])
|(?P<rightBracker>[)])
|(?P<nonTerminal>(Sx|A_aug|A_sim|A_dro|Ao|Ex|Fun|Par|Pas|Lla|El|Or_l|And_l|Not_l|Lx|Lo|Or_b|Xor_b|And_b|Shift|Ax|Af|Ap|At|Si|Dc|Ctrl|For|While|If))
|(?P<endStatement>[;])
|(?P<identifier>ID)
|(?P<droneFunction>(move_to|rotate))
|(?P<updater>(\+=|-=|\*=|/=|%=|>>=|<<=|&=|\|=|\^=|\*\*=))
|(?P<comparatorLarger>(<=|>=|==|!=))
|(?P<operatorLarger>(\|\| | && | \*\*))
|(?P<operator>(\+ | - | ~ | \* | % | / | >> | << | & | \| | \^ | !))
|(?P<comparator>(< | >))
|(?P<list>list\()
|(?P<pointOfInterest>poi\()
|(?P<number>NUMBER)
|(?P<string>STRING)
|(?P<epsilon>[ε])
|(?P<reservedWord>(while|if|for|else|elif))
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
|(?P<comma>[,])
|(?P<equal>[=])
|(?P<string>(?P<quote>['"]).*?(?P=quote))
"""

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
