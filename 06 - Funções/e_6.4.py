# Exercício 6.4 Crie uma função que receba dois argumentos nomeados: nome e idade. A função
# deve imprimir na tela uma mensagem a seu gosto contendo o nome e a idade da pessoa.

def imprimirMsg(nome: str, idade: int) -> None:
    print(f'Nome : {nome}\nIdade : {idade}')


imprimirMsg(idade=20, nome='murilo')