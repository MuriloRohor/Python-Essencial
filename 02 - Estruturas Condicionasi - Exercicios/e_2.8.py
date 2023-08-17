# Exercício 2.8 Escreva um programa que verifique se uma string é um número real ou não (pode usar estrutura de repetição).

s = input("Digite numero inteiro: ")
eh_real = True
ponto_encontrado = False

for char in s:
     if char == '.':
         if ponto_encontrado:
             eh_real = False
             break
         ponto_encontrado = True
     elif not char.isdigit():
         eh_real = False
         break
       
if eh_real:
    print("A string é um número real")
else:
    print("A string não é um número real")