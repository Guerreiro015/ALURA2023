#REMOVENTO DUPLICATAS
#VAMOS CRIAR UM CLASSE PARA cONTER OS dADOS QUE TEM NAS OUTRAS DUAS CLASSES

# Usando o IF e for pra imprimir todos os detalhes dos objetos filmes e series

import os
os.system("cls")
class programa:
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



class Filme(programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
      

    

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f"Nome: {vingadores.nome}, Likes: {vingadores.likes}")
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
print(f"Nome: {vingadores.nome}- Likes: {vingadores.likes}")

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}')
atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}')


filmes_series = [vingadores,atlanta]


# Usando o for pra imprimir todos os detalhes do objetos filmes e series
for programa in filmes_series:
    if hasattr(programa, 'duracao'):
        detalhes = "Duração: ",programa.duracao

    elif hasattr(programa, 'temporadas'): 
        detalhes = ("Quant. de Temporadas: ",programa.temporadas)
    else:
        detalhes = ""
    
    print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')

# melhorando para mão precisar usar usar o for e if