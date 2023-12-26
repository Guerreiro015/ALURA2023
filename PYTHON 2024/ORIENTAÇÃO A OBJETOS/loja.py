from avaliacao import Avaliacao


class lojas():
    lista_restaurante=[]
    def __init__(self,nome,categoria):       
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._ativo=False
        self._avaliacao=[]
        lojas.lista_restaurante.append(self)
    
    def __str__(self):
        return f'Nome do Restaurante: {self._nome} \nCategoria do Restaurante {self._categoria}\nSituação do Restaurante: {self.ativo}\n'
    
    def mostrar():
        for i in lojas.lista_restaurante:
            print(f'\nNome: {i._nome.ljust(15)}\nCategoria: {i._categoria.ljust(15)}\nSituação: {i.ativo}\nAvaliacao: {lojas.media_avaliacoes}\n')



    @classmethod
    def listar_restaurantes(cls):
        
        for restaurante in cls.lista_restaurante:
            print(f'\n{restaurante._nome.ljust(25)} | \n{restaurante._categoria.ljust(25)} | \n{str(lojas.media_avaliacoes).ljust(25)} |\n{restaurante.ativo}')


        
    @property
    def ativo(self):
        return ' ⊙  Ativado ✔️ 🤪' if self._ativo==True else " ⊗  Desativado 🚫🤪"
   
    def alternar(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    
# japones=lojas('Plaza','novo')
# chines=lojas('SUSHI','Peixe')
# italiano=lojas('MONALIZA','Pizza')

# japones.alternar()
# italiano.alternar()


# rest=[japones,chines]


# for i in rest:
#     print(f'Nome do Restaurante: {japones.nome} \nCategoria do Restaurante {japones.categoria}\nSituação do Restaurante {japones.ativo}\n')

portugal=lojas('Delicia','bacalhau')
portugal.alternar()

portugal.receber_avaliacao('Gui', 10)
portugal.receber_avaliacao('Lais', 10)
portugal.receber_avaliacao('Emy', 10)
portugal.receber_avaliacao('Fran', 10)


lojas.listar_restaurantes()
lojas.mostrar()

# print(chines)
# print(italiano)


