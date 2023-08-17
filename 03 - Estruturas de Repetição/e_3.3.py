# Exercício 3.3 Imprima todos os números ímpares de 1 a 100.

for n in range(1, 101):
    if n % 2 != 0:
        print(n, end=" ")