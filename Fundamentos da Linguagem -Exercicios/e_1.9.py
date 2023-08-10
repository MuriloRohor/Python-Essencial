# Exercício 1.9 Peça ao usuário para digitar um número e calcule o seno, cosseno e tangente desse número. 
import math

n = int(input("Digite um número: "))

print(f"Seno de {n} = {math.sin(n):.2f}")
print(f"Cosseno de {n} = {math.cos(n):.2f}")
print(f"Tangente de {n} = {math.tan(n):.2f}")