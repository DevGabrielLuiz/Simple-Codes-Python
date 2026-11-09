# função decoradas e decoradores
# Decorar = adicionar / remover / restringir / alterar
# dcoradores são usados para fazer o python usar ad funções decoradas em outras funções

def create_function(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args: 
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@create_function
def invert_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
invert_string_checando_paramentro = criar_funcao(invert_string)
invertida = invert_string_checando_paramentro('123')
invertida = invert_string_checando_paramentro(123)
print(invertida)

# Decoradores são Sintax Sugar

# inner function e nexted function - função externa