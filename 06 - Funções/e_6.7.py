# Exercício 6.7 Crie uma função que receba uma lista como argumento e retorne o maior valor da lista. 

lista = list(range(1, 11))

def maiorValorLista(lista: list) -> int:
    return max(lista)

print(maiorValorLista(lista))