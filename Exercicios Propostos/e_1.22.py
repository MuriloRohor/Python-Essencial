# Exercício 1.22 Peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto e calcule a velocidade média do objeto

ds = float(input("Distância Percorrida: "))
dt = float(input("Tempo Gasto: "))

vm = ds / dt

print(f"Velocidade Média: {vm:.2f}")