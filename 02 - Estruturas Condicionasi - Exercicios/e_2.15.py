# Exercício 2.15 Escreva um programa que pergunte ao usuário seu salário e exiba uma mensagem
# de “Alto salário” se o salário for maior do que R$10.000,00, ou “Baixo salário” caso contrário.

salario = float(input("Digite seu salário: "))

if salario > 10000:
    print(f"R$ {salario:.2f} - Alto salário")
else:
    print(f"R$ {salario:.2f} - Baixo salário")