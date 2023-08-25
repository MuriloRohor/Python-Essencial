# Exercício 3.8 Calcule o fatorial de um número digitado pelo usuário
n = int(input("Digite um nº: "))
fatorial = n
while True:
    if (fatorial > 0):
        print(f"{n}! -> {n} x {fatorial} = {n * fatorial}")
        fatorial -= 1
        continue
    break