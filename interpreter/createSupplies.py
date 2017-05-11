from .lexicalAnalysis.lexicalAnalyzer import Token
from .aParser.semantic_functions import semantic_functions
import os

##################### Global variables ####################
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
"""
###################################################

class Supplier(object):

	def __init__(self):
		self.rules = {}
		self.grammar = {}
		tokenizer = Token(grammarPattern)
		module_dir = os.path.dirname(__file__)
		filepath = os.path.join(module_dir, 'grammophone.txt')
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
				has_semantic = True if int(indexRule) in semantic_functions else False
				self.grammar[indexRule] = rule, tokens, has_semantic
		module_dir = os.path.dirname(__file__)
		file_path = os.path.join(module_dir, 'aParser\\grammar.py')
		f = open(file_path, 'w')
		f.write('grammar = {\n')
		for indexRule in self.grammar:
			f.write("\t" + str(indexRule) + " : " + repr(self.grammar[indexRule]) + ",\n")
		f.write('}\n')
		f.close()

	def getGrammar(self):
		return self.grammar

	def getRules(self):
		return self.rules

	def getSemantic(self):
		return semantic_functions
