# Exercício 1.12 Peça ao usuário para digitar o raio de um círculo e calcule a área e o comprimento do círculo.
import math

raio = float(input("Informe o raio de um círculo: "))

a = math.pi * raio ** 2
p = 2 * math.pi * raio

print(f"O círculo de raio {raio:.1f}, possuí o perímetro de {p:.2f} e área de {a:.2f}")