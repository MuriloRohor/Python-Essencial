# Exercício 6.6 Crie uma função que receba uma lista como argumento e adicione um elemento à
# lista dentro da função. Em seguida, imprima a lista fora da função para verificar se o elemento foi adicionado corretamente.

lista = list(range(0,10))
def adicionarElementoList(lista: list) -> None:
    lista.append('Teste')
    print(f"Print dentro da função | {lista}")

adicionarElementoList(lista)
print(f"Print fora da função | {lista}")