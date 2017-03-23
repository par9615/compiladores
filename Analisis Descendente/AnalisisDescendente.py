stack = []
inputString = '(int+int)*)int+int'
tokens = []
terminals = ["int", "+","*","(",")"]
nonTerminals = ["E","E'","T","T'", "F"]
initial = "E"
firstS = ["(", "int"]

matrix = {
    "E": {
        "int" : ["T","E'"] ,
        "("  : ["T","E'"],
        ")"  : ["sync"],
        "$"  : ["sync"]
    },
    "E'": {
        "+"  : ["+","T","E'"],
        ")"  : ["eps"],
        "$"  : ["eps"]
    },
    "T": {
        "int" : ["F", "T'"],
        "+"  : ["sync"],
        "("  : ["F","T'"],
        ")"  : ["sync"],
        "$"  : ["sync"]
    },
    "T'" : {
        "+"  : ["eps"],
        "*"  : ["*", "F", "T'"],
        ")"  : ["eps"],
        "$"  : ["eps"]
        },
    "F" : {
        "int"  : ["int"],
        "+"  : ["sync"],
        "*"  : ["sync"],
        "("  : ["(", "E", ")"],
        ")"  : ["sync"],
        "$"  : ["sync"]
        }
}


"""
E -> TE'
E'-> +TE' | eps
T -> FU
U -> *FU | eps
F -> (E) | id
"""
def isTerminal(symbol):
    if(symbol in terminals):
        return True
    else:
        return False

def insertRule(top, token):
    global stack
    global matrix
    reversedRule = reversed(matrix[top][token])
    for value in reversedRule:
        stack.append(value)

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


########################

getTokens(inputString)

stack.append("$")
stack.append("E")            #inicializar la stack
coincidence = ''               #incializar coincidencias


output = ["", "", "", ""]

print("{:>16}\t{:>16}\t{:>16}\t{:<16}\n".format("Coincidencia", "stack", "Entrada", "Accion"))

del output[:]

while(len(stack)):
    output.append(coincidence)

    output.append("".join(reversed(stack)))

    output.append("".join(tokens))

    top = stack.pop()                            #se obtiene el primero de la stack
    token = tokens[0]                        #se obtiene el token del principio

    if(top == token):
        tokens.pop(0)
        coincidence += token
        output.append("Coincidencia " + token)

    elif(top == '$'):
        # Pila vacía -> meter inicial a la pila y hacer pop en tokens hasta que encuentre uno que este en su first
        stack.append("$")
        stack.append(initial)
        while(tokens[0] not in firstS):
            tokens.pop(0)
        output.append("Pila vacía, borrar hasta token in First(S)")

    elif(token in matrix[top]):
        if ("#" in matrix[top][token]):
            output.append("Salida " + top + " -> #")
        else: #Checar si es SYNC dentro de este else -> se omite el top
            if "sync" in matrix[top][token]:
                output.append("Error: M[" + top + "," + token + "] = sync, " + "pop(" + top + ")")
            elif "eps" in matrix[top][token]:
                output.append("Salida " + top + " -> " + "".join(matrix[top][token]))
            else:
                insertRule(top, token)
                output.append("Salida " + top + " -> " + "".join(matrix[top][token]))

    else: #Aqui se revisa si el error fue M[top,token] o si top != token
        if token not in matrix[top]:
            tokens.pop(0)
            stack.append(top)
            output.append("Error: Símbolo omitido")
        else:
            output.append("pop(" + top + ")")

    print("{:>16}\t{:>16}\t{:>16}\t{:<16}".format(output[0], output[1], output[2], output[3]))
    del output[:]

    if (len(stack) == 0):
        print("Aceptado")
