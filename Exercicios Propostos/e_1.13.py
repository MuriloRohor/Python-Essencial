# Exercício 1.13 Peça ao usuário para digitar as dimensões de um retângulo (largura e altura) e calcule a área e o perímetro desse retângulo.
b = float(input("Digite a base do triângulo: ")) 
h = float(input("Digite a altura do triângulo: "))

area = (b * h) / 2
perimetro = b * 3

print(f"\nÁrea Triângulo: {area}\nPerímetro Triângulo: {perimetro}")