# Exercício 2.13 Escreva um programa que verifique se uma pessoa é elegível para aposentadoria
# (se tem 60 anos ou mais para mulheres e 65 anos ou mais para homens).

print("Qual é seu sexo?\n1 - Homem\n2 - Mulher") 
s = int(input("Digite a opção: "))
idade = int(input("Digite sua idade: "))

if s == 1 and idade >= 65:
    print("Você pode aposentar!")
elif s == 2 and idade >= 60:
    print("Você pode aposentar!")
else:
    print("Não atende os requisitos da aposentadoria!")