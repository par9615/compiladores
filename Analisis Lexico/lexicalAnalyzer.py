import re

token_pattern = r"""
(?P<terminal>[a-z])
|(?P<nonTerminal>[A-Z])
|(?P<identifier>[a-zA-Z_][a-zA-Z0-9_]*)
|(?P<epsilon>[#])
|(?P<integer>[0-9]+)
|(?P<dot>\.)
|(?P<open_variable>[$][{])
|(?P<open_curly>[{])
|(?P<close_curly>[}])
|(?P<newline>\n)
|(?P<operator>([+]|[-]))
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

stuff = r'A id a b + - = 1'

print(' stuff '.center(60, '='))
for tok in tokenize(stuff):
    print(tok)