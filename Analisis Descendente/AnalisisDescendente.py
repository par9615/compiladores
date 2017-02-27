pila = []
token = ["id","+","(","+","id","$"]
terminales = ["id", "+","*","(",")"]
noTerminales = ["E","T","X","Y"]
inicial = "E"

matriz = {
    "E": {
        "id" : "TX" ,
        "("  : "TX"
    },
    "T": {
        "("  : "(E)",
        "id"  : "id"
    },
    "X": {
        ")" : "#",
        "+"  : "+E",
        "$"  : "#"
    },
    "Y" : {
        ")"  : "#",
        "+"  : "#",
        "*"  : "*E",
        "$"  : "#"
        }
}


"""
E -> TE'
E'-> +TE' | eps
T -> FU
U -> *FU | eps
F -> (E) | id

"""
def isTerminal(simbolo):
    if(simbolo in terminales):
        return True
    else:
        return False

def insertRule(top, nextToken):
    global pila
    global matriz
    rule = (matriz[top][nextToken])[::-1]
    singleQuote = False
    if rule == 'di':
        pila.append('id')
        return
    for c in rule:
        pila += c
        if c == "'":
            singleQuote = True
            pila.pop()
        elif singleQuote:
            value = pila.pop() + "//'"
            pila.append(value)
            singleQuote = False

########################
#analisis sintactico


#lista[::-1]    ->  invierte la lista
#''.join(list)  ->  convierte la lista en un solo string


pila += "$"+ inicial            #inicializar la pila
coincidencia = ''               #incializar coincidencias


output = []

print("{:>12}\t{:>12}\t{:>12}\t{:<12}\n".format("Coincidencia", "Pila", "Entrada", "Accion"))

while(len(pila)):
    #print(coincidencia, end = " \t\t")      #imprime coincidencia
    output.append(coincidencia)

    output.append("".join(reversed(pila)).replace('/', ''))
    #for i in reversed(pila):                #imprime pila
    #    for j in i:
    #        if(j != "/"):
    #            print(j, end = "")


    #print("\t\t", end = "")

    output.append("".join(token))
    #for i in token:                         #imprime tokens de entrada
        #print(i, end = "")

    #print("\t\t", end = "")

    top = pila.pop()                            #se obtiene el primero de la pila
    nextToken = token[0]                        #se obtiene el token del principio

    if(top == nextToken):
        token.pop(0)
        coincidencia += nextToken
        output.append('Coincidencia ' + nextToken)
        #print('Coincidencia ' + nextToken)

    elif (top != '$' and nextToken in matriz[top].keys()):
        if (matriz[top][nextToken] != "#"):
            insertRule(top,nextToken)
            output.append('Salida ' + top.replace('/', '') + ' ->' + matriz[top][nextToken])
            #print('Salida ' + top + ' ->' + matriz[top][nextToken])

        else:
            output.append('Nada')
            #print("Nada")

    else:
        output.append('Error')
        print("{:>12}\t{:>12}\t{:>12}\t{:<12}".format(output[0], output[1], output[2], output[3]))
        #print('Error')
        break

    if('$' in output[3]):
        output[3] = 'Aceptado'

    print("{:>12}\t{:>12}\t{:>12}\t{:<12}".format(output[0], output[1], output[2], output[3]))
    del output[:]
    #print (pila)
