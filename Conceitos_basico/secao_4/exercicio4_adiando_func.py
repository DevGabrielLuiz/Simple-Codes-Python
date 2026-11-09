def soma(x,y):
    return x + y

def multiplica(x, y):
    return x * y

# este jeito esta com erro
# def criar_func(funcao, *args): 
    return funcao(*args)

#soma_com_5 = criar_func(soma, 5)
#multiplica_por_dez =criar_func(multiplica, 5)

def criar_func(funcao, x): 
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_5 = criar_func(soma, 5)
multiplica_por_dez =criar_func(multiplica, 5)

print(soma_com_5(10))
print(multiplica_por_dez(3))