
# IMPORTANDO AS CLASSES ABSTRATOS QUE JA EXISTEM

# import os
# os.system("cls")

# from collections.abc import MutableSequence
# class Playlist(MutableSequence):
#     pass

# filmes = Playlist()
 
#  # VAI SOLICITAR PRA USAR OS METODOS
# #TypeError: Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert

# from numbers import Complex
# class Numero(Complex):
#   pass  


# filme = Numero()

# from numbers import Complex
# class Numero(Complex):
#     def __getitem__(self, item):
#         super().__getitem__()


# filme = Numero()

from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

lista = MinhaListagem('Nova_lista')
print(lista)

#  o método acima que faltou foi o __len__, que caracteriza a classe abstrata Sized.


#Apenas com isso abaixo, podemos garantir que o __str__ será implementado nas nossas subclasses, se não for implementado em alguma, será avisado em tempo de instanciação (não vai conseguir criar instâncias).
from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass