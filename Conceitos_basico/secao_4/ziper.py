#Exercicio unir listas
# Crie função zipper que ira unir duas listas

# deve usar todos os valores da menor lista
#l4[i]= (l1[i],l2[i])
from itertools import zip_longest


l1 = ['Belo Horizonte', 'Santos', 'Manaus']
l2 = ['MG', 'SP', 'AM']

# Resultado esperado:
[('Belo Horizonte', 'MG'), ('Santos', 'SP'), ('Manaus', 'AM')]
l4 = []
for i in l2:
    l4[i]= (l1[i],l2[i])
l3 = zipper(l2, l1)
print(l4)

# RESOLUCAO
def zipper(lista1, lista2):
    intervalo = (min(len(lista1),len(lista2)))
    return [(l1[1], l2[i]) for i in range(intervalo)]

print(zipper(l1, l2))

from itertools import zip_longest
# retorna um iterator entao temos que percorrer com for ou usar função de lista
print(zip(l1,l2)) 
print(list(zip_longest(l1,l2, fillvalue='SEM CIDADE')))
