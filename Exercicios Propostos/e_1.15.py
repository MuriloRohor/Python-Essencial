# Exercício 1.15 Peça ao usuário para digitar a distância e a velocidade inicial de um objeto em queda livre 
# e calcule o tempo que ele leva para atingir o solo, desconsiderando a resistência do ar.
import math

d = float(input("Distância: "))
v = float(input("Velocidade: "))
g = 9.81


t = (v + math.sqrt(v**2 + 2*g*d)) / g

print(f"O objeto irá levar {t:.2f} para atingir o solo...")