#REMOVENTO DUPLICATAS
#VAMOS CRIAR UM CLASSE PARA cONTER OS dADOS QUE TEM NAS OUTRAS DUAS CLASSES

# 
## usando a classe para pecrorre a playlist
# retirando a função (list) list é funçao built in
# retirado  o  super().__init__(programa)


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

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
    


vingadores = Filme('vingadores - guerra infinita', 2018, 168)

print(f"Nome: {vingadores.nome}, Likes: {vingadores.likes}")
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
print(f"Nome: {vingadores.nome}- Likes: {vingadores.likes}\n")

atlanta = Serie('atlanta', 2018, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}')
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}\n')

tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_series = [vingadores,atlanta,demolidor,tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_series)

print(f'Tamanho do playlist: {playlist_fim_de_semana.tamanho}')
print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana.listagem}')

## melhorando para não precisar usar usar o IF
for programas in playlist_fim_de_semana.listagem:
    print(programas)
