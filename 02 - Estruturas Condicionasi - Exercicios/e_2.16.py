# Exercício 2.16 Escreva um programa que pergunte ao usuário seu gênero (M para masculino, F para feminino) 
# e exiba uma mensagem de “Gênero masculino” ou “Gênero feminino”.

genero = input("Digite seu Gênero (F/M): ")

if genero.lower() == 'f':
    print("Gênero Feminino!")

elif genero.lower() == 'm':
    print("Gênero Masculino!")

else:
    print("Digite uma sigla valída!")
