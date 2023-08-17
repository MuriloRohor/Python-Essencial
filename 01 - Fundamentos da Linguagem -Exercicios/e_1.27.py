# Exercício 1.27 Leia o nome, o salário e o valor do imposto de uma pessoa como entrada e imprimir o salário líquido.
n = input("Nome Pessoa: ")
s = float(input("Salario: "))
i = float(input("Imposto(%): "))

i = s * i/100
s -= i


print(f"Nome: {n}\nImposto Pago R$ {i:.2f}\nSalário Líquido: R$ {s:.2f}")