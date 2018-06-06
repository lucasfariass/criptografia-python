listaLetras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                "r", "s", "t", "u", "v", "w", "x", "y", "z"]

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                17, 18, 19, 20, 21, 22, 23, 24, 25, 0]

tabelaNumeros = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
tabelaNumerosInversos = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

a = 2
b = 5
c = 1
d = 3

matrizSenha = [[ a, b], [ c, d]]

frase = str(input("Digite a frase: "))
frase1 = str(input("Digite o codigo: "))

def getFraseDecodificada(frase):
    paresDeLetras = getParesDeLetras(frase)
    fraseDecodificada = ""

    for par in paresDeLetras:
        valorLetraUm = getValorLetra(par[0])
        valorLetraDois = getValorLetra(par[1])

        fraseDecodificada += getLetrasCriptografadas(valorLetraUm, valorLetraDois, getMatrizInversa(a, b, c, d))

    return fraseDecodificada
    

def getMatrizInversa(a, b, c, d):
    detA = (a * d) - (b * c) 

    for i in range(len(tabelaNumeros)):
        if detA == tabelaNumeros[i]:
            detA = tabelaNumerosInversos[i]
            break

    copiaMatrizSenha = [[ d, (b*-1)], [ (c*-1), a]]
    matrizInversa = []
    vetorAux = []

    for linha in copiaMatrizSenha:
        for coluna in linha:
            elemento = coluna * detA
            if elemento >= 0:
                elemento = elemento % 26
            else:
                elemento = 26 - ((elemento * (-1)) % 26)
            vetorAux.append(elemento)
            
        matrizInversa.append(vetorAux)
        vetorAux = []

    return matrizInversa
        
def getFraseCriptografada(frase):
    paresDeLetras = getParesDeLetras(frase)
    fraseCriptografada = ""

    for par in paresDeLetras:
        valorLetraUm = getValorLetra(par[0])
        valorLetraDois = getValorLetra(par[1])

        fraseCriptografada += getLetrasCriptografadas(valorLetraUm, valorLetraDois, matrizSenha)

    return fraseCriptografada
        
def getParesDeLetras(frase):
    paresDeLetras = []
    parLetras = ""

    if len(frase) % 2 != 0:
        frase += frase[-1]
            
    for letra in frase: 
        if letra != " ":
            parLetras += letra
            if len(parLetras) == 2:
                paresDeLetras.append(parLetras)
                parLetras = ""

    return paresDeLetras
                                 

def getValorLetra(letra):
    for i in range(len(listaLetras)):
        if letra == listaLetras[i]:
            return listaNumeros[i]
           

def getLetrasCriptografadas(valorLetraUm, valorLetraDois, matrizSenha):
    valorCriptUm = (matrizSenha[0][0] * valorLetraUm + matrizSenha[0][1] * valorLetraDois)
    valorCriptDois = (matrizSenha[1][0] * valorLetraUm + matrizSenha[1][1] * valorLetraDois)
    
    if valorCriptUm >= 0:
        valorCriptUm = valorCriptUm % 26
    else:
        valorCriptUm = 26 - ((valorCriptUm * (-1)) % 26)

    if valorCriptDois >= 0:
        valorCriptDois = valorCriptDois % 26
    else:
        valorCriptDois = 26 - ((valorCriptDois * (-1)) % 26)

    letrasCript = ""
    primeiraLetra = ""
    segundaLetra = ""

    temPrimeira = False
    temSegunda = False
    for i in listaNumeros:
        if i == valorCriptUm:
            primeiraLetra += listaLetras[i-1]
            temPrimeira = True
        elif i == valorCriptDois:
            segundaLetra += listaLetras[i-1]
            temSegunda = True
        elif temPrimeira and temSegunda:
            break

    letrasCript = primeiraLetra + segundaLetra     
    return letrasCript

print(getFraseCriptografada(frase))
print(getFraseDecodificada(frase1))





