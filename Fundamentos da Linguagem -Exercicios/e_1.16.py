# Exercício 1.16 Peça ao usuário para digitar o valor inicial de um investimento, a taxa de juros e o
# número de anos e calcule o valor final do investimento considerando juros compostos

c = float(input("Valor Investimento: "))
i = float(input("Taxa de Juros(Mês): "))
a = float(input("Quantos anos: "))

m = c * (1 + i) ** a

print(f"Investimento de : {m:.2f}")


