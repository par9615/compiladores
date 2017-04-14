import re

token_pattern = r"""
(?P<leftCurly>[{])
|(?P<rightCurly>[}])
|(?P<leftBracket>[(])
|(?P<rightBracker>[)])
|(?P<reservedWord>(while|if|for))
|(?P<twoPoints>[:])
|(?P<updater>(\+=|-=|\*=|/=|%=|>>=|<<=|&=|\|=|\^=|\*\*=))
|(?P<operatorDouble>(\|\| | &&))
|(?P<operator>(\+ | - | ~ | \* | \*\* | % | / | >> | << | & | \| | \^) )
|(?P<comparatorLarger>(<=|>=|==|!=))
|(?P<comparator>(< | >))
|(?P<endStatement>[;])
|(?P<nonTerminal>[A-Z][a-z]+)
|(?P<identifier>[a-zA-Z_][a-zA-Z0-9_]*)
|(?P<float>[0-9]?\.[0-9]+)
|(?P<integer>[0-9]+)
|(?P<dot>\.)
|(?P<newline>\n)
|(?P<whitespace>\s+)
|(?P<equals>[=])
|(?P<slash>[/])
"""

token_re = re.compile(token_pattern, re.VERBOSE)

class TokenizerException(Exception): pass

def tokenize(text):
    pos = 0
    while True:
        m = token_re.match(text, pos)
        if not m: break
        pos = m.end()
        tokname = m.lastgroup
        tokvalue = m.group(tokname)
        yield tokname, tokvalue
    if pos != len(text):
        raise TokenizerException('tokenizer stopped at pos %r of %r' % (
            pos, len(text)))


stuff = r'; = += *= >>= < > | || & &&'

print(' stuff '.center(60, '='))
print(stuff)
for tok in tokenize(stuff):
    print(tok)