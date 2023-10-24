

# IMPORTANDO AS CLASSES ABSTRATOS QUE JA EXISTEM

import os
os.system("cls")
import aula8_objeto2
from collections.abc import MutableSequence
class Playlist(MutableSequence):
    pass


class Playlist():
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    @property
    def listagem(self):
        return self._programa

    @property
    def tamanho(self):
        return len(self._programa)
    
for programa in aula8_objeto2.Playlist:
    print(programa)

#############################################################
# class Playlist():
#     def __init__(self, nome, programa):
#         self.nome = nome
#         self._programa = programa

#     def __getitem__(self, item):
#         return self._programa[item]

#     def __len__(self):
#         return len(self._programa)

# for programa in aula8_objeto2.Playlist:
#     print(programa)