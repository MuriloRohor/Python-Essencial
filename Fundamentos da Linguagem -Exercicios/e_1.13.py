# Exercício 1.13 Peça ao usuário para digitar as dimensões de um retângulo (largura e altura) e calcule a área e o perímetro desse retângulo.

l = float(input("Digite a largura do retângulo: ")) 
h = float(input("Digite a altura do retângulo: "))

area = (l * h) 
perimetro = (l * 2) + (h * 2) 

print(f"\nÁrea retângulo: {area}\nPerímetro retângulo: {perimetro}")