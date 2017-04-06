stack = []
inputString = ""
tokens = []
symbols = []
terminals = ["a", "b", "c"]
nonTerminals = []
initial = 0

matrix = {
    0 : {
        "a":   "S2",
        "S" :   "G1"
    },

    1: {
        "$":    "AC"
    },

    2: {
        "b":    "S4",
        "c":    "R2",
        "$":    "R2",
        "A":    "G3"
    },

    3: {
        "c":    "R1",
        "$":    "R1"
    },

    4: {
        "b":   "S5"
    },

    5: {
        "a":    "S2",
        "S":    "G6"
    },

    6: {
        "c":   "S7"
    },

    7: {
        "c":   "R3",
        "$" :   "R3"
    }
}

grammar = {
        1: ("S", ["a","A"]),
        2:  ("A",[]),
        3: ("A",["b","b","S","c"])
}

follow = {
    "S": ["$", "c"],
    "A": ["$", "c"]
}

def getTokens(inputString):
    i = 0
    while (i < len(inputString)):
        character = inputString[i]
        if (character == ' '):
            i+=1
        for terminal in terminals:
            count = 0
            for letter in terminal:
                if (i < len(inputString) and letter == inputString[i]):
                    i += 1
                    count += 1
                else:
                    break
            if (count == len(terminal)):
                tokens.append(terminal)
                break
    tokens.append('$')

def pushNextState(top, token):  #Hace un push en la pila del estado en matrix[top][token] -> "S5" hace stack.append(5)
    global stack
    state = getState(top,token)
    stack.append(state)

def shift(top, token):   #No hace nada
    global stack

def reduce(top, token): #Hace todo el procedimiento del reduce
    global stack
    global symbols

    rule  = grammar[getState(top,token)][1]
    head = grammar[getState(top,token)][0]

    for i in range(0, len(rule)):
        stack.pop()
        symbols.pop()

    pushNextState(stack[-1], head)
    symbols.append(head)

    return [head, "".join(rule)]

def action(top, token):             #Retorna la acción en matrix[top][token] -> "S5" return "S"
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




####################################

inputString = input("Escriba entrada \n>")

getTokens(inputString)

stack.append(initial)

formattedString = "{:>13}\t{:>13}\t{:>13}\t{:>15}"

print(formattedString.format("Pila", "Simbolos", "Entrada", "Acción"))
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
