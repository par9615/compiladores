from lexicalAnalysis.lexicalAnalyzer import *

rules = {
	'Sx' : {
		'A_aug;Sx' : 0,
		'A_sim;Sx' : 1,
		'A_dro;Sx' : 2,
		'A_aug;' : 3,
		'A_sim;' : 4,
		'A_dro;' : 5,
		'CtrlSx' : 6,
		'Ctrl' : 7
	},
	'A_aug' : {
		'IDAoEx': 8
	},
	'A_sim' : {
		'ID=Ex' : 9
	},
	'A_dro' : {
		'IDDc' : 10
	},
	'Ao' : {
		'+=' : 11,
		'-=' : 12,
		'*=' : 13,
		'/=' : 14,
		'%=' : 15,
		'>>=' : 16,
		'<<=' : 17,
		'&=' : 18,
		'|=' : 19,
		'^=' : 20,
		'**=' : 21
	},
	'Ex' : {
		'Or_l' : 22
	},
	'Or_l' : {
		'Or_l||And_l' : 23,
		'And_l' : 24
	},
	'And_l' : {
		'And_l&&Not_l' : 25,
		'Not_l' : 26
	},
	'Not_l' : {
		'!Not_l' : 27,
		'Lx' : 28
	},
	'Lx' : {
		'LxLoOr_b' : 29,
		'Or_b' : 30
	},
	'Lo' : {
		'<' : 31,
		'>' : 32,
		'<=' : 33,
		'>=' : 34,
		'==' : 35,
		'!=' : 36
	},
	'Or_b' : {
		'Or_b|Xor_b' : 37,
		'Xor_b' : 38
	},
	'Xor_b' : {
		'Xor_b^And_b' : 39,
		'And_b' : 40
	},
	'And_b' : {
		'And_b&Shift' : 41,
		'Shift' : 42
	},
	'Shift': {
		'Shift>>Ax' : 43,
		'Shift<<Ax' : 44,
		'Ax' : 45
	},
	'Ax' : {
		'Ax+Af' : 46,
		'Ax-Af' : 47,
		'Af' : 48
	},
	'Af' : {
		'Af*Ap' : 49,
		'Af%Ap' : 50,
		'Af/Ap' : 51,
		'Ap' : 52
	},
	'Ap' : {
		'At**Ap' : 53,
		'At' : 54
	},
	'At' : {
		'SiNUMBER' : 55,
		'STRING' : 56,
		'SiID' : 57,
		'Si(Ex)' : 58
	},
	'Si' : {
		'+' : 59,
		'-' : 60,
		'~' : 61,
		'#' : 62
	},
	'Dc' : {
		'=**(STRING,NUMBER)**' : 63,
		'-<(Ex,Ex,Ex)' : 64,
		'-)(Ex,Ex,Ex)' : 65
	},
	'Ctrl' : {
		'For' : 66,
		'While' : 67,
		'If' : 68
	},
	'For' : {
		'for(ID:(Ex,Ex)){Sx}' : 69
	},
	'While' : {
		'while(Ex){Sx}' : 70
	},
	'If' : {
		'if(Ex){Sx}' : 71,
		'if(Ex)else{Sx}' : 72
	}
}

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Grammar(object):
	__metaclass__ = Singleton

	def __init__(self,grammarPattern):
		self.grammar = {}
		tokenizer = Token(grammarPattern)
		for rule in rules:
			for production in rules[rule]:
				indexRule = rules[rule][production]
				self.grammar[indexRule] = (rule, tokenizer.tokenizeText(production))


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
|(?P<number>NUMBER)
|(?P<string>STRING)
|(?P<epsilon>\#)
|(?P<reservedWord>(while|if|for))
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
"""


grammar = Grammar(grammarPattern)
print(grammar.grammar)