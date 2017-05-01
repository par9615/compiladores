import re

from .helper_functions import grammarPattern

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

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Grammar(object):
	__metaclass__ = Singleton

	def __init__(self):
		self.rules = {}
		self.grammar = {}
		self.matrix = {}
		tokenizer = Token(grammarPattern)
		current_path = os.path.abspath(__file__)
		filepath = os.path.abspath(os.path.join(current_path, "..", "..", "grammophone.txt"))
		with open(filepath, 'r') as grammoFile:
			counter = 0
			for line in grammoFile:
				if not('->' in line) or '#' in line:
					continue
				noSpaces = line.replace('.','').replace('\n', '').replace(' o ', ' | ').replace('oo', '||').replace('o=','|=')
				arrowIndex = noSpaces.index('->')
				head = noSpaces[:arrowIndex].strip()
				ruleString = noSpaces[arrowIndex + len('->'):]
				if not(head in self.rules):
					self.rules[head] = {}
				self.rules[head][ruleString.strip()] = counter
				counter += 1

		for rule in self.rules:
			for production in self.rules[rule]:
				tokens = []
				for tupleToken in tokenizer.tokenizeText(production):
					tokensParsed = list(tupleToken)
					if (tokensParsed[0] == 'orDetected'):
						tokensParsed[1] = tokensParsed[1].replace('o', '|')
					tokens.append(tokensParsed[1])

				hasSemantic = True if (type(self.rules[rule][production]) is dict and 'semantic' in self.rules[rule][production]) else False
				indexRule, semantic = None, None
				if (hasSemantic):
					indexRule = self.rules[rule][production]['number']
					semantic = self.rules[rule][production]['semantic']
					self.grammar[indexRule] = rule, tokens, semantic
				else:
					indexRule = self.rules[rule][production]
					self.grammar[indexRule] = rule, tokens


	def getGrammar(self):
		return self.grammar

	def getRules(self):
		return self.rules