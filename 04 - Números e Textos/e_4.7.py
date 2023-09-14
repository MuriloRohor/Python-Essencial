# Exercício 4.7 Crie um programa que peça ao usuário para digitar um nome de usuário e uma senha
# contendo apenas caracteres alfanuméricos e use expressão regular para fazer uma limpeza nos
# valores digitados, exibindo-os novamente para o usuário os valores que forem modificados

import re

def limpar_string(s):
    """Limpa a string removendo caracteres não alfanuméricos."""
    return re.sub(r'[^a-zA-Z0-9]', '', s)

def main():
    # Solicita ao usuário um nome de usuário e senha
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Limpa o nome de usuário e senha
    nome_usuario_limpo = limpar_string(nome_usuario)
    senha_limpa = limpar_string(senha)

    # Verifica se os valores foram modificados e exibe para o usuário
    if nome_usuario != nome_usuario_limpo:
        print(f"Nome de usuário modificado: {nome_usuario_limpo}")
    if senha != senha_limpa:
        print(f"Senha modificada: {senha_limpa}")

if __name__ == "__main__":
    main()

