from lexicalAnalysis.lexicalAnalyzer import *
import os

##################### Functions ####################
def semantic9():
	print('Semantic 9')

def semantic8():
	print('Semantic 8')

def semantic46():
	print('Semantic 46')

####################################################

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Grammar(object):
	__metaclass__ = Singleton

	def __init__(self, grammarPattern):
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
				head = noSpaces[:arrowIndex]
				ruleString = noSpaces[arrowIndex + len('->'):]
				if not(head in self.rules):
					self.rules[head] = {}
				self.rules[head][ruleString.lstrip()] = counter
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