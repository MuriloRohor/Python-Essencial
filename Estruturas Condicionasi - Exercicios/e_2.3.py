# Exercício 2.3 Escreva um programa que verifique se uma letra digitada pelo usuário é uma vogal ou consoante.

VOGAL = ['a', 'e', 'i', 'o', 'u']

l = input("Digite uma letra: ")

if l in VOGAL:
    print(f"A letra {l} é uma vogal.")
else:
    print(f"A letra {l} é uma consoante.")