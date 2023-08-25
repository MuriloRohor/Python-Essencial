# Exercício 3.7 Calcule a média dos números digitados pelo usuário. O usuário deve digitar números até digitar um número negativo. 
lista_numeros = []

while True:
    n = int(input("Digite um nº: "))
    if (n < 0):
        break
    else:
        lista_numeros.append(n)
        media = sum(lista_numeros) / len(lista_numeros)
        print(f"Média : {media}")
    
    
