# Exercício 1.14 Peça ao usuário para digitar a base e a altura de um triângulo e calcule a área desse triângulo.

b = float(input("Digite a base do triângulo: ")) 
h = float(input("Digite a altura do triângulo: "))

area = (b * h) / 2 
perimetro = b * 3

print(f"\nÁrea triângulo: {area}\nPerímetro triângulo: {perimetro}")