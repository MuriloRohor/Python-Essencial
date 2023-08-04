# Exercício 1.11 Peça ao usuário para digitar três números e calcule a fórmula de Bhaskara para esses números
import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

DELTA = b ** 2 - 4 * a * c

print(f"x¹ = {(( b * -1)  +  math.sqrt(DELTA)) / ( 2 * a )}")
print(f"x² = {(( b * -1)  -  math.sqrt(DELTA)) / ( 2 * a )}")
