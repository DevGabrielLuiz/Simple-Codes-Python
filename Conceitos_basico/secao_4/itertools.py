# Combinadores, Permutations e Product
# Combinação - ordem nao importa - iteravel + tamanho do grupo

#permutação - ordem importa

#produto - ordem import e repete valores unicos 



from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
pessoas = [
    'Joao', 'Joana' , 'luiz', 'leticia'
]
camisetas = [
    ['preta', 'branca']
]

print_iter((combinations(pessoas,2)))
print_iter((permutations(pessoas,2)))
print_iter((product(pessoas,2)))