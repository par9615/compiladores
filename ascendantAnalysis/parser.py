from ascendantAnalysis.grammar import Singleton
from lexicalAnalysis.lexicalAnalyzer import *

class Parser(object):
	__metaclass__ = Singleton

	def __init__(self, pattern):
		self.tokenizer = Token(pattern)

	def parseInput(self, text):
		parsedLanguage = []
		for tupleToken in self.tokenizer.tokenizeText(text):
			if (tupleToken[0] == 'identifier'):
				parsedLanguage.append('ID')
			elif (tupleToken[0] == 'number'):
				parsedLanguage.append('NUMBER')
			elif (tupleToken[0] == 'whitespace'):
				continue
			else:
				parsedLanguage.append(tupleToken[1])
		return parsedLanguage
