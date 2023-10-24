#REMOVENTO DUPLICATAS
#VAMOS CRIAR UM CLASSE PARA cONTER OS dADOS QUE TEM NAS OUTRAS DUAS CLASSES

# 
## melhorando para mão precisar usar usar o IF

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
    
    def imprime(self):
        print(f'Nome: {programa.nome}  - Likes: {programa.likes}')
    



class Filme(programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {programa.nome} - Duração: {self.duracao} Minutos - Likes: {programa.likes}')
        

    

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Nome: {programa.nome} - Temporadas: {self.temporadas} - Likes: {programa.likes}')
    

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


filmes_series = [vingadores,atlanta]


## melhorando para mão precisar usar usar o IF
for programa in filmes_series:
    programa.imprime()
    
    # if hasattr(programa, 'duracao'):
    #     detalhes = "Duração: ",programa.duracao

    # elif hasattr(programa, 'temporadas'): 
    #     detalhes = ("Quant. de Temporadas: ",programa.temporadas)
    # else:
    #     detalhes = ""
    
    # print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')

