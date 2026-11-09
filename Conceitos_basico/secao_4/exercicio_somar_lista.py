#Some os valores nas listas retornando uma nova lista com os valores somados:
 
# se uma lista for maior que a outra, a soma vai considerar o tamanho da menor
# Resolução propia
lista_1 = [11, 33 ,34, 43]
lista_2 = [32, 2, 34, 5, 65, 343, 445]
lista_3 = []
#for i in range(len(lista_1)):
#    lista_3.append(lista_1[i]+lista_2[i])
#
#print(lista_3) 
    

#from itertools import zip_longest
#print(list(zip_longest(lista_1,lista_2,fillvalue=None)))

# Mais 'pythonico
for i, _ in enumerate(lista_1): # retorna so valor sem indice
    lista_3.append(lista_1[i]+lista_2[i])
print(lista_3) 

#Full python

lista_soma = [x + y for x,y in zip(lista_1, lista_2)]
print(lista_soma)
