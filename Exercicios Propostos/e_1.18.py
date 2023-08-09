# Exercício 1.18 Peça ao usuário para digitar a massa e a aceleração de um objeto e calcule a força resultante

m = float(input("Massa Objeto: "))
a = float(input("Aceleração Objeto: "))

f = m * a 

print(f"Força Resultante : {f:.2f} N")