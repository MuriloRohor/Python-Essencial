# Exercício 2.6 Escreva um programa que verifique se uma string é um palíndromo ou não (não usarestrutura de repetição). 

def eh_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]


frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")