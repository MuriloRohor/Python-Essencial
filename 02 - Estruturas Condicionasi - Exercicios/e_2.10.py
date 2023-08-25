# Exercício 2.10 Escreva um programa que calcule a média de três números e exiba uma mensagem
# de “Aprovado” se a média for maior ou igual a 6, ou “Reprovado” caso contrário. Se a nota for 10, exiba também a mensagem “Parabéns”.

numeros = list()

while True:
    n = int(input("Digite um número : "))
    numeros.append(n)
    if len(numeros) < 3:
        continue

    media = sum(numeros) / len(numeros)
    if media >= 9:
        print(f"Parabéns : {media:.2f}")
        break
    elif media >= 6:
        print(f"Aprovado : {media:.2f}")
        break
    else:
        print(f"Reprovado : {media:.2f}")
        break