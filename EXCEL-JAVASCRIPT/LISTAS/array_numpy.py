import os
os.system("cls")

import array as arr

teste = arr.array('d', [1, 3.5])

print(teste)
# Esta função interna array não é utilizada.

# em vez disso usamos o numpy

import numpy as np

teste = np.array([1.,3.4,5.])# Parenteses e dentro lista com colchetes

print(teste)

tsste=teste+5


# Faltou importar o que eu tenho que importar. Para isso,
#  eu faço from abc import ABCMeta, abstractmethod.
#  Usamos o ABCmeta como uma meta classe, metaclass.
#  É uma configuração que precisamos colocar: class Conta(metaclass=ABCMeta):.
#  O abstractmethod já está no nosso código, mais abaixo.

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

