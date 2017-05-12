import re

##################### Patterns #####################
languagePattern = r"""
(?P<drone>drone)
|(?P<string>((?P<quote>['"]).*?(?P=quote)))
|(?P<leftCurly>[{])
|(?P<rightCurly>[}])
|(?P<leftBracket>[(])
|(?P<rightBracker>[)])
|(?P<endStatement>[;])
|(?P<droneFunction>(move_to|rotate))
|(?P<updater>(\+=|-=|\*=|/=|%=|>>=|<<=|&=|\|=|\^=|\*\*=))
|(?P<comparatorLarger>(<=|>=|==|!=))
|(?P<operatorLarger>(\|\| | && | \*\*))
|(?P<operator>(\+ | - | ~ | \* | % | / | >> | << | & | \| | \^ | !))
|(?P<comma>[,])
|(?P<comparator>(< | >))
|(?P<list>list\()
|(?P<pointOfIntereset>poi\()
|(?P<float>[0-9]?\.[0-9]+)
|(?P<number>[0-9]+)
|(?P<reservedWord>(while|if|for|else|elif))
|(?P<identifier>[a-zA-Z_$][a-zA-Z_$0-9]*)
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
|(?P<equal>[=])
"""
####################################################

class TokenizerException(Exception): pass

class Token(object):
    def __init__(self,pattern): 
        self.token_re = re.compile(pattern, re.VERBOSE)

    def tokenizeText(self, text):
        position = 0
        tokens = []
        while True:
            result = self.token_re.search(text, position)
            if not result: break
            position = result.end()
            token_group = result.lastgroup
            token_value = result.group(token_group)
            tokens.append((token_group, token_value))
        if position != len(text):
            raise TokenizerException('Tokenizer stopped at position {} of {} from {}'.format(position, len(text), text))
        return tokens



inputStrings = ["a = 3+4;",
			   "b *= 6", 
				"c = b <= a", 
				"x = 1^0", 
				"y = x & z", 
				"mod_x = x%10",
				"inputString = 'Bjorn_drone'",
				'location = "128.52.21.03"',
				"x_pow = 2**8", 
				"if(1>0){x += 1}", 
				"for(i : arr){i **= 3}",
				"x = -1.3"]

inputToken = Token(languagePattern)


for i in inputStrings:
	#print(str(i))
	print('\n', 'Input: ', i, '\nTokenized input: ', inputToken.tokenizeText(i))
