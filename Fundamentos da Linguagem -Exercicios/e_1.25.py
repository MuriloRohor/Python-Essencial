# Exercício 1.25 Calcule o volume de uma esfera dado o seu raio como entrada.
import math

r = float(input("Raio Esfera: "))
v = (4/3) * math.pi * (r ** 3)

print(f"Volume Esfera: {v:.2f} m³")