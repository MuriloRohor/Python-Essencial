# Exercício 6.5 Crie uma função que defina uma variável x dentro da função e imprima o valor de x
# na tela. Em seguida, chame a função e verifique se a variável x está acessível fora da função. 

def definirVariavel() -> None:
    x = 'Variável X'
    print(x)

# print(x) -> NameError: name 'x' is not defined