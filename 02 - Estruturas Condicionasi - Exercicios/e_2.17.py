# Exercício 2.17 Escreva um programa que pergunte ao usuário seu peso e altura e exiba uma
# mensagem de “Você está abaixo do peso” se o IMC (índice de massa corporal) for menor do que
# 18,5, “Você está com o peso normal” se o IMC estiver entre 18,5 e 24,9, “Você está com sobrepeso”
# se o IMC estiver entre 25 e 29,9, ou “Você está com obesidade” caso contrário.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Você está abaixo do peso!")

elif imc < 24.9 and imc > 18.5:
    print("Você está com o peso normal!")

elif imc < 29.9 and imc > 25:
    print("“Você está com obesidade")