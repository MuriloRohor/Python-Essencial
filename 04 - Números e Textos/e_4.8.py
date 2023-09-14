# Exercício 4.8 Crie um programa que peça ao usuário para digitar uma frase com 5 palavras. Caso
# a frase digitada tenha uma quantidade diferente de palavras, o usuário deve digitar novamente. Ao
# fim, mostre uma palavra por linha. Use tokenização para extrair as palavras.

def obter_frase():
    """Solicita ao usuário uma frase com 5 palavras. Retorna a frase se ela tiver 5 palavras, caso contrário, pede novamente."""
    while True:
        frase = input("Digite uma frase com 5 palavras: ")
        palavras = frase.split()

        if len(palavras) == 5:
            return palavras
        else:
            print("A frase deve conter exatamente 5 palavras. Tente novamente.")

def main():
    palavras = obter_frase()

    # Exibe cada palavra em uma linha separada
    for palavra in palavras:
        print(palavra)

if __name__ == "__main__":
    main()
