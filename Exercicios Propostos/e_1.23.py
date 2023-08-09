# Exercício 1.23 Peça ao usuário para digitar a distância percorrida, o tempo gasto e a aceleração de um objeto e calcule a velocidade inicial e final.
ds = float(input("Distância Percorrida: "))
dt = float(input("Tempo Gasto: "))
va = float(input("Aceleração(m/s²): "))

vf = va * dt
vi = vf - va * dt

print(f"Velocidade Inicial : {vi:.2f} m/s\nVelocidade Final : {vf:.2f} m/s")