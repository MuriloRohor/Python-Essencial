# Exercício 1.30 Crie dois conjuntos e combine-os usando as operações de união, interseção e diferença, apresentando os resultados de cada operação.
a = [1, 2, 3]
b = [3, 4, 5]

conjA = set(a)
conjB = set(b)

print(f"Uniao : {conjA.union(conjB)}")
print(f"Intersecao : {conjA.intersection(conjB)}")
print(f"Diferenca : {conjA.difference(conjB)}")