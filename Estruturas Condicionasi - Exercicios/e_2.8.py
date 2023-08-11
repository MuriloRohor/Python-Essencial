# Exercício 2.8 Escreva um programa que verifique se uma string é um número real ou não (pode usar estrutura de repetição).
str_ = input("Numero: ")

if str_.isnumeric():
     n = int(str_)
     if n > -1:
          print("é um numero real")
else:
     print("Não é um numero inteiro")