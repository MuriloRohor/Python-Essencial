# Exercício 2.11 Escreva um programa que verifique se uma temperatura está acima, abaixo ou 
# dentro da faixa normal (36°C a 37°C). 

temp = float(input("Digite sua temperatura: "))

if (temp > 37):
    print("Temperatura acima do normal!")
elif (temp < 36):
    print("Temperatura abaixo do normal!")
else:
    print("Temperatura normal!")