from modelos.cardapio.item_cardapio import Item_cardapio

class Prato(Item_cardapio):
    def __init__(self,nome,preco,descricao,tamanho):
        super().__init__(nome,preco)
        self._descricao=descricao
        self._tamanho=tamanho
        
    def __str__(self):
        return f'Prato do dia: {self._nome} por apenas: {self._preco}'



    
def main():
 pass
    
if __name__ == '__main__':
    main()
   
