# Exercício 2.7 Escreva um programa que verifique se uma string é um número inteiro ou não e
# mostre uma mensagem de acordo (pode usar estrutura de repetição). 

s = input("Digite numero inteiro: ")
eh_inteiro = True

for char in s:
    if not char.isdigit():
        eh_inteiro = False
        break
if eh_inteiro:
    print("A string é um número inteiro")
else:
    print("A string não é um número inteiro")