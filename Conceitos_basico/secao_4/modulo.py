# O primeiro módulo a ser executado sempre se chama __main__
# Pode importar outro módulo inteiro ou parte desse módulo
# O python conhece a pasta onde o main e está e as pastas abaixo dele 
# não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
print('Este módulo se chama', __name__)

from tkinter import Y

import metodos_string 
 
from tipos_valores import falso

print(falso)
__all__ = [
    x, y
]
# Tudo que estiver dentro da lista all, variaveis metodos sera importado e tudo que estiver fora nao vai ser importado
from secao_4 import 
