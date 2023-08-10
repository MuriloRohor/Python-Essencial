# Exercício 2.7 Escreva um programa que verifique se uma string é um número inteiro ou não e
# mostre uma mensagem de acordo (pode usar estrutura de repetição). 

frase = input("Frase: ").replace('\b'),
palindromo = list(frase)
palindromo.reverse()

palindromo = ''.join(palindromo)

if palindromo == frase:
    print(f"{frase}")
    print(f"{palindromo}")
    print("É um palíndromo")

else:
    print(f"{frase}")
    print(f"{palindromo}")
    print("Não é um palíndromo")