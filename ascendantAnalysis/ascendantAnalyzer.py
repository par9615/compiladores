################### Imports ########################
from ascendantAnalysis.grammar import *
from ascendantAnalysis.matrix import *
from ascendantAnalysis.parser import *
from lexicalAnalysis.lexicalAnalyzer import *
####################################################


##################### Patterns #####################
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
|(?P<epsilon>\#)
|(?P<reservedWord>(while|if|for|else))
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
|(?P<comma>[,])
|(?P<equal>[=])
"""

languagePattern = r"""
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
|(?P<identifier>[a-zA-Z_$][a-zA-Z_$0-9]*)
|(?P<updater>(\+=|-=|\*=|/=|%=|>>=|<<=|&=|\|=|\^=|\*\*=))
|(?P<comparatorLarger>(<=|>=|==|!=))
|(?P<operatorLarger>(\|\| | && | \*\*))
|(?P<operator>(\+ | - | ~ | \* | % | / | >> | << | & | \| | \^ | !))
|(?P<comparator>(< | >))
|(?P<number>([0-9]?.[0-9]+|[0-9]+))
|(?P<string>[\"])
|(?P<epsilon>\#)
|(?P<reservedWord>(while|if|for|else))
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
|(?P<comma>[,])
|(?P<equal>[=])
"""
####################################################


##################### Functions ####################
def contains(l, filter):
    function = False
    for value in l:
        if filter(value):
            function = True
            break
    return function

def getInitial(grammar):
   index = grammar.keys()
   return min(index)

def pushNextState(top, token):  #Hace un push en la pila del estado en matrix[top][token] -> "S5" hace stack.append(5)
    global stack
    state = getState(top,token)
    stack.append(state)

def shift(top, token):   #No hace nada
    global stack

def reduce(top, token): #Hace todo el procedimiento del reduce
    global stack
    global symbols

    production = grammar[getState(top, token)]

    rule  = production[1]
    head = production[0]

    if (not(len(rule) == 1 and rule[0] == '#')):
        for i in range(0, len(rule)):
            stack.pop()
            symbols.pop()
        symbols.append(head)

    pushNextState(stack[-1], head)

    if (len(production) == 3 and contains(production, lambda value : hasattr(value, '__call__'))):
        production[2]()

    return [head, "".join(rule)]

def action(top, token):             #Retorna la accion en matrix[top][token] -> "S5" return "S"
    action = matrix[top][token]
    return action

def getState(top, token):           #Retorna el estado en matrix[top][token] -> "S5" return int(5)
    return int(matrix[top][token][1:])

def handleError(top):
    global stack
    global follow
    global tokens
    global symbols

    A = "S"
    inputToken = tokens[0]
    s = top

    while(not(A in matrix[s])):
        stack.pop()
        s = stack[-1]

    while(not(inputToken in follow[A])):
        tokens.pop(0)
        inputToken = tokens[0]


    stack.append(getState(s,A))

    symbols.append(A)

def algorithm(inputString):
    global tokens
    tokens = parser.parseInput(inputString)

    stack.append(initial)

    formattedString = "{:>20}\t{:>20}\t{:>20}\t{:>20}"

    print(formattedString.format("Pila", "Simbolos", "Entrada", "Accion"))
    output = []
    token = tokens[0]

    while(1):
        output.append(" ".join(map(str,stack)))

        output.append("".join(symbols))

        output.append("".join(tokens))

        top = stack[-1]

        if(token in matrix[top]):
            act = action(top, token)

            if("S" in act): #Shift
                pushNextState(top,token)
                symbols.append(token)
                tokens.pop(0)
                token = tokens[0]
                output.append("Shift " + act[1:])

            elif("R" in act): #Reduce
                rule = reduce(top,token)
                output.append("Reduce " + rule[0] + " -> " + rule[1])

            elif("A" in act): #Aceptado
                output.append("Aceptado")

            else:
                handleError(top)
                token = tokens[0]
                output.append("Error T")

        else:
            handleError(top)
            token = tokens[0]
            output.append("Error T")

        print(formattedString.format(output[0], output[1], output[2], output[3]))

        if (output[-1] == "Aceptado"):
            break;

        del output[:]
####################################################


################# Global variables #################
stack = []
symbols = []
tokens = []
grammarParsed = Grammar(grammarPattern)
grammar = grammarParsed.getGrammar()
parser = Parser(languagePattern)
initial = getInitial(grammar)
####################################################