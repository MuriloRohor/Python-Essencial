# Exercício 6.9 Crie uma função recursiva que calcule o fatorial de um número inteiro.

def fatorial(n):
    """Calcula o fatorial de um número inteiro n usando recursão."""
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Testando a função
num = int(input("Digite um número inteiro: "))
print(f"Fatorial de {num} é {fatorial(num)}")
