# Exercício 1.17 Peça ao usuário para digitar o preço de uma mercadoria, o desconto e o imposto e calcule o preço final da mercadoria. 

m = float(input("Preço Produto: "))
d = float(input("Desconto Produto(%): "))
i = float(input("Imposto Produto(%): "))




f = m - (m * (d/100))
f += (f * (i/100))

print(f"Preço Produto: {m:.2f}\nImposto: {i} %\nDesconto: {d} %\nPreço Final: {f:.2f}")