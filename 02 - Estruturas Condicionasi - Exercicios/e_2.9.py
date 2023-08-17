# Escreva um programa que verifique se uma string digitada pelo usuário é uma data no formato mm/dd/aaaa ou não.

data = input("Data: ")
if len(data) == 10:
    data.split('/')
    if data[0] > 0 and data[0] < 32:
        dia = True
    elif data[1] > 0 and data[1] < 13:
        mes = True
    elif data[2] > 0 and data[2] < 10000:
        ano = True

if ano == True and mes == True and dia == True:
    print(f"O formarto de data está carreto")
else: 
    print("O formato não está correto")