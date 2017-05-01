from ..lexicalAnalysis.lexicalAnalyzer import Token
from .semantic_functions import semantic_functions
import os

##################### Global variables ####################
grammarPattern = r"""
(?P<droneDeclarationStart>=\*\*\()
|(?P<droneDelcarationEnd>\)\*\*)
|(?P<moveDeclaration>-<)
|(?P<rotateDeclaration>-\))
|(?P<leftCurly>[{])
|(?P<rightCurly>[}])
|(?P<leftBracket>[(])
|(?P<rightBracker>[)])
|(?P<nonTerminal>(Sx|A_aug|A_sim|A_dro|Ao|Ex|Or_l|And_l|Not_l|Lx|Lo|Or_b|Xor_b|And_b|Shift|Ax|Af|Ap|At|Si|Dc|Ctrl|For|While|If))
|(?P<endStatement>[;])
|(?P<identifier>ID)
|(?P<updater>(\+=|-=|\*=|/=|%=|>>=|<<=|&=|\|=|\^=|\*\*=))
|(?P<comparatorLarger>(<=|>=|==|!=))
|(?P<operatorLarger>(\|\| | && | \*\*))
|(?P<operator>(\+ | - | ~ | \* | % | / | >> | << | & | \| | \^ | !))
|(?P<comparator>(< | >))
|(?P<number>NUMBER)
|(?P<string>STRING)
|(?P<epsilon>[ε])
|(?P<reservedWord>(while|if|for|else))
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
|(?P<comma>[,])
|(?P<equal>[=])
"""
###################################################

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
		tokenizer = Token(grammarPattern)
		current_path = os.path.abspath(__file__)
		filepath = os.path.abspath(os.path.join(current_path, "..", "..", "grammophone.txt"))
		with open(filepath, 'r') as grammoFile:
			counter = 0
			for line in grammoFile:
				if not('->' in line) or '#' in line:
					continue
				noSpaces = line.replace('\n', '').replace(' o ', ' | ').replace('oo', '||').replace('o=','|=')
				arrowIndex = noSpaces.index('->')
				head = noSpaces[:arrowIndex].strip()
				ruleString = noSpaces[arrowIndex + len('->'):-1].strip()
				if not(head in self.rules):
					self.rules[head] = {}
				if (len(ruleString) == 0):
					ruleString = 'ε'
				self.rules[head][ruleString.replace(' ', '')] = counter
				counter += 1

		for rule in self.rules:
			for production in self.rules[rule]:
				tokens = []
				for tupleToken in tokenizer.tokenizeText(production):
					tokensParsed = list(tupleToken)
					tokens.append(tokensParsed[1].encode("utf-8"))

				indexRule = self.rules[rule][production]
				has_semantic = True if indexRule in semantic_functions else False
				self.grammar[indexRule] = rule, tokens, has_semantic
		module_dir = os.path.dirname(__file__)
		file_path = os.path.join(module_dir, 'grammar.py')
		f = open(file_path, 'w')
		f.write('grammar = ' + repr(self.grammar) + '\n')
		f.close()

	def getGrammar(self):
		return self.grammar

	def getRules(self):
		return self.rules

	def getSemantic(self):
		return semantic_functions