# Exercício 1.20 Peça ao usuário para digitar o valor da medida de um ângulo em radianos e calcule o valor desse ângulo em graus.
import math

r = float(input("Angulo em Radianos: "))
g = r * (180 / math.pi)

print(f"Graus : {g:.2f}º")