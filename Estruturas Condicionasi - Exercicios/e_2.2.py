# Exercício 2.2 Escreva um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero

n = int(input("Número: "))

if n > 0:
    print(f"{n} é Positivo")
elif n < 0:
    print(f"{n} é Negativo")
else:
    print(f"{n} é 0")
    
