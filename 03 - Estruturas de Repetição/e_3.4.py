# Exercício 3.4 Soma todos os números de 1 a 100
soma = 0
for i in range(0, 101):
    soma += i
    print(f"{i} + {soma - i} = {soma}")
