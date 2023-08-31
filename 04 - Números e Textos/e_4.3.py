# Exercício 4.3 Crie um programa que peça ao usuário para inserir um ângulo em graus e calcule o seno, cosseno e tangente desse ângulo.
import math

a = int(input("Digite um angulo º: "))

print(f'Seno : {math.sin(a):.2f}')
print(f'cosseno  : {math.cos(a):.2f}')
print(f'tangente : {math.tan(a):.2f}')