# Exercício 1.4 Peça ao usuário para digitar seu peso e altura, calcule o índice de massa corporal (IMC) e imprima o resultado.

p = int(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

imc = p / (a ** 2)
print(f"Seu IMC : {imc}")



