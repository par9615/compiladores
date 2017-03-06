stack = []
tokens = ["int", "*", "(", "int", "+" , "int", ")", ")" "$"]
symbols = []
terminals = []
nonTerminals = []
initial = 0

matrix = {
    0 : {
        "int":   "S4",
        "(" :   "S3" ,
        "E" :   "G1",
        "T" :   "G2"
    },

    1: {
        "$":    "AC"
    },

    2: {
        "+":    "S6",
        ")":    "R5",
        "$":    "R5",
        "X":    "G5"
    },

    3: {
        "int":    "S4",
        "(":    "S3",
        "E":    "G7",
        "T":    "G2"
    },

    4: {
        "+":   "R7",
        "*" :   "S11",
        ")" :   "R7",
        "$" :   "R7",
        "Y" :   "G10"
    },

    5: {
        "+":   "R1",
        ")" :   "R1",
        "$" :   "R1"
    },

    6: {
        "int":   "S4",
        "(" :   "S3",
        "E" :   "G8",
        "T" :   "G2"
    },

    7: {
        ")":   "S9"
    },

    8:  {
        "+":    "R4",
        ")":    "R4",
        "$":    "R4"
    },

    9:  {
        "+":    "R2",
        ")":    "R2",
        "$":    "R2"
    },

    10: {
        "+":    "R3",
        ")":    "R3",
        "$":    "R3"
    },

    11: {
        "int":  "S4",
        "(":    "S3",
        "T":    "G12"
    },

    12: {
        "+":    "R6",
        ")":    "R6",
        "$":    "R6"
    }
}

grammar = {
        1: ("E", ["T","X"]),
        2:  ("T",["(", "E", ")"]),
        3: ("T",["int", "Y"]),
        4: ("X", ["+", "E"]),
        5: ("X", []),
        6: ("Y",["*", "Y"]),
        7: ("Y", [])
}

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

####################################

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
            output.append("Shift " + act[1])

        elif("R" in act): #Reduce
            rule = reduce(top,token)
            output.append("Reduce " + rule[0] + " -> " + rule[1])

        elif("A" in act): #Aceptado
            output.append("Aceptado")

        else:
            output.append("Error")

    else:
        output.append("Error")

    print(formattedString.format(output[0], output[1], output[2], output[3]))

    if (output[-1] == "Error" or output[-1] == "Aceptado"):
        break;

    del output[:]
