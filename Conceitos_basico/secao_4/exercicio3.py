# Exercícios
# Aumente os preços dos produtos em 10% 

produtos = [
    {'nome': 'Produto 3', 'preco':  12.56},
    {'nome': 'Produto 5', 'preco':  34.65},
    {'nome': 'Produto 4', 'preco':  23.89},
    {'nome': 'Produto 2', 'preco':  82.11},   
    {'nome': 'Produto 1', 'preco':  47.88},
]
# Ordene os produtos por nome decrescente 
# Gere produtos_ordenados_por_nome por deep copy (copia profunda )

# Ordena os produtos por preco crescente 
# Gere produtos_ordenados_por_preco por deep_copy 
import copy

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)


produtos_preco = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print(*produtos, sep='\n')
print()
print(*produtos_preco, sep='\n')
