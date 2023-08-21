# Exercício 2.14 Escreva um programa que verifique se um número inteiro digitado pelo usuário é
# divisível por outro número inteiro digitado pelo usuário ou não.

n = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if (n % n2 == 0):
    print(f"{n} / {n2} é divisivel!")
else: 
    print("Não é divisivel")