# Exercício 1.19 Peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de transição de uma para outra e calcule a aceleração.

vi = float(input("Velocidade Inicial: "))
vf = float(input("Velocidade Final: "))
dt = float(input("Tempo Transição: "))

a = (vf - vi) / dt

print(f"Aceleração : {a:.2f}")