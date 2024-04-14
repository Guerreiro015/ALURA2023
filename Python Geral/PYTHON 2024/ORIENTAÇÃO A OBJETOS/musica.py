
class musica():
    lista_musica=[]
    def __init__(self,nome_musica,cantor, duracao):
        self.nome_musica=nome_musica
        self.cantor=cantor
        self._duracao=duracao
        musica.lista_musica.append(self)

    def __str__(self):
        return(f'MUSICA: {self.nome_musica.ljust(20)} CANTOR: {self.cantor.ljust(20)} DURACAO: {self.duracao}')
        
    def listar():
        for i in musica.lista_musica:
           print(f'MUSICA: {i.nome_musica.ljust(20)} CANTOR: {i.cantor.ljust(20)} DURACAO: {i.duracao}')
        print('\n')
   
    @property
    def duracao(self):
        return f' 💗 Duração Pequena' if self._duracao=='1:34' or self._duracao=='1:45' else ' 😂 Duração Longa'
    

music1=musica('Amor de Paixao','Antonio Show','1:34')
music2=musica('Forro danado','Sanfona de OUro','2:05')
music3=musica('Paixao Proibida','Trio de Três','1:45')
music4=musica('Peito Aberto','Cacto do Nordeste','2:11')


musica.listar()
print(music1)