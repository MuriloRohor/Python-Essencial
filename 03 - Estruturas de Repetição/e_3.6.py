# Exercício 3.6 Soma todos os números ímpares de 1 a 100.
soma = 0
for i in range(0, 101):
    if (i % 2 != 0):
        soma += i
        print(f"{i} + {soma - i} = {soma}")