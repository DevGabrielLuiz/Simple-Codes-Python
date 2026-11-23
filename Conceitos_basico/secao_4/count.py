# count é um iterator sem fim (itertools)
from itertools import count
c1 = count() # ele não é do própio python é do itertools
r1 = range(10)
print(next(c1))
print(next(c1))

print(hasattr(c1,'__iter__'))
# entrega o valor e soma mais 1

for i in c1:
    if i > 10:
        break 
    print(i)
print('testando', 'iterator',sep='---------')

c2 = count(5, 5) # mesma coisa
r2 = range(5, 50, 5)

for i in c2:
    print(c2)
    if i >=50:
        break