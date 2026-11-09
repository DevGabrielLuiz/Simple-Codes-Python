from threading import local


def fora(x):
    a = x 
    def dentro():
        print(locals()) # retorna as variaveis locais 
    
        return a 
    return dentro
# o a é variavel livre pois nao esta definido dentro da função interna

dentro_teste1 = fora(10)
dentro_teste2 = fora(20)

print(dentro_teste1())

# Variaveis livres + nonlocal (locals, globals)
print(globlas())

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        valor_final += valor_a_concatenar # da erro pois a variavel nao é daquela funcao 
        return valor_final
    return interna
c = concatenar('a') # sem fazer nada aprenas retorna 
