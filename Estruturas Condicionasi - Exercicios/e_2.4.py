# Exercício 2.4 Escreva um programa que verifique se um ano é bissexto ou não (pesquise o que caracteriza um ano como bissexto).

ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto")
else: 
    print(f"{ano} não é um ano bissexto")
    