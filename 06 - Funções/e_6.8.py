# Exercício 6.8 Crie uma função que receba uma string como argumento e retorne essa string invertida, mostrando-a ao final. 

def inverterString(s: str) -> str:
    listaString = list(s)
    listaInvertidaString = listaString[::-1]
    stringInvertida = ''.join(listaInvertidaString)

    return stringInvertida

print(inverterString('Murilo'))
