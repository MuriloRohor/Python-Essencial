# Exercício 1.21 Peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo e calcule o comprimento da hipotenusa.
import math

lme = float(input("Lado menor: "))
lma = float(input("Lado maior: "))

calc = lme ** 2 + lma ** 2

c = math.sqrt(calc)

print(f"Cateto : {c}")