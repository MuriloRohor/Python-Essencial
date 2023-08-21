# Exercício 2.12 Escreva um programa que verifique se uma pessoa pode votar ou não (se tem 18 anos ou mais e se é brasileira).

nac = input("Digite sua Nacionalidade: ")
idade = int(input("Digite sua Idade: "))

if (nac.lower() == "brasileira" and idade >= 18):
    print("Você pode votar!")

else:
    print("Você não pode votar!")