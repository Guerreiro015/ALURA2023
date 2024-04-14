#REMOVENTO DUPLICATAS
#VAMOS CRIAR UM CLASSE PARA cONTER OS dADOS QUE TEM NAS OUTRAS DUAS CLASSES

# 
## usando a classe para percorrer a playlist
# retirando a função (list) list é funçao built in
# retirado  o  super().__init__(programa)
# acrescentado o __getitem__(self)
# retirado propiedade tamanho e acrescentado __len__(self)
# habilitando o len para ser usado 

import os
os.system("cls")
class programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self):
        return (f'Nome: {programas.nome}  - Likes: {programas.likes}')
    


class Filme(programas):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return(f'Nome: {programas.nome} - Duração: {self.duracao} Minutos - Likes: {programas.likes}')
        

    

class Serie(programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return(f'Nome: {programas.nome} - Temporadas: {self.temporadas} - Likes: {programas.likes}')


# class Playlist(list):
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)

#     def tamanho(self):
#         return len(self.programas)

    
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self,item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

  
    def __len__(self):
        return len(self._programas)
    


vingadores = Filme('vingadores - guerra infinita', 2018, 168)

atlanta = Serie('atlanta', 2018, 2)

tmep = Filme('Todo mundo em pânico', 1999, 100)

demolidor = Serie('Demolidor', 2001, 5)
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()


filmes_series = [vingadores,atlanta,demolidor,tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_series)

# Usando o _getitem__ podemos usar o ( for in e o in )
# Não precisa usar .tamanho e .listagem

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}') 

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana.listagem}') 

## melhorando para não precisar usar usar o IF
for programas in playlist_fim_de_semana.listagem:
    print(programas)

   
   
    # Há outras formas:

# Para quê?         	Método
# Inicialização	        __init__
# Representação	        __str__, __repr__
# Container, sequência	__contains__, __iter__, __len__, __getitem__
# Numéricos	            __add__, __sub__, __mul__, __mod__

# temos o seguinte:

# Para quê?	Como?
# Inicialização	        obj = Novo()
# Representação	        print(obj), str(obj), repr(obj)
# Container, sequência	len(obj), item in obj, for i in obj, obj[2:3]
# Numéricos	            obj + outro_obj, obj * obj