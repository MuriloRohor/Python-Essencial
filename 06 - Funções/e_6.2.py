# Exercício 6.2 Crie uma função que receba um número como argumento e retorne True se o número for par e False se o número for ímpar.

def verificarPar(n: int) -> bool:
    if (n % 2 == 0):
        return True
    else:
        return False