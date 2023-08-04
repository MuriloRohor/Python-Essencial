# Exercício 1.7 Peça ao usuário para digitar o nome, o preço de custo, o preço de venda e a quantidade
# em estoque de determinado produto e mostre o lucro que esse estoque pode gerar se todos os produtos forem vendidos.

np = input("Nome Produto: ")
pc = float(input("Custo Produto: "))
pv = float(input("Preço Produto: "))
qe = int(input("Quantidade Estoque: "))

def LucroProduto(pc: float, pv: float, qe: int) -> float:
    lp = pv * qe - pc * qe
    return lp;

def TelaConsole():
    print(f"Produto   |   Custo   |   Preço   |   QNTD EST   |   LUCRO TOTAL\n{np}         {pc}       {pv}         {qe}             {LucroProduto(pc, pv, qe)}")

TelaConsole();


