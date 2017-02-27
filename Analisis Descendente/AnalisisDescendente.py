stack = []
tokens = ["int","*","(","int","+","int",")",")","$"]
terminals = ["int", "+","*","(",")"]
nonTerminals = ["E","T","X","Y"]
initial = "E"

matrix = {
    "E": {
        "int" : ["T","X"] ,
        "("  : ["T","X"]
    },
    "T": {
        "("  : ["(","E",")"],
        "int"  : ["int", "Y"]
    },
    "X": {
        ")" : ["#"],
        "+"  : ["+","E"],
        "$"  : ["#"]
    },
    "Y" : {
        ")"  : ["#"],
        "+"  : ["#"],
        "*"  : ["*","E"],
        "$"  : ["#"]
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


########################


stack.append("$")
stack.append("E")            #inicializar la stack
coincidence = ''               #incializar coincidencias


output = ["", "", "", ""]

print("{:>12}\t{:>12}\t{:>12}\t{:<12}\n".format("Coincidencia", "stack", "Entrada", "Accion"))

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
        output.append("Error")

    elif(token in matrix[top]):
        if ("#" in matrix[top][token]):
            output.append("Salida " + top + " -> #")
        else:
            insertRule(top, token)
            output.append("Salida " + top + " -> " + "".join(matrix[top][token]))

    else:
        output.append("Error")

    print("{:>12}\t{:>12}\t{:>12}\t{:<12}".format(output[0], output[1], output[2], output[3]))
    if (output[3] == "Error"): break
    del output[:]

    if (len(stack) == 0):
        print("Aceptado")
