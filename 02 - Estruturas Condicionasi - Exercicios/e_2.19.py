# Exercício 2.19 Escreva um programa que peça ao usuário para digitar 5 números inteiros. O
# programa deve exibir uma mensagem informando se todos os números digitados são pares ou se
# há pelo menos um número ímpar.

for i in range(0,5):
    n = int(input("Digite um nº: "))
    if (n % 2 != 0):
        print("Existe pelo menos um número ìmpar!")
        break
    elif (i < 4):
        continue
    print("Todos os números são pares!")
    