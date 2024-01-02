from modelos.cardapio.item_cardapio import Item_cardapio

class Bebida(Item_cardapio):
    def __init__(self,nome,preco,tamanho,descricao):
        super().__init__(nome,preco)
        self._tamanho=tamanho
        self._descricao=descricao

    def __str__(self):
        return f'Suco de {self._nome} por apenas: {self._preco}'





def main():
 pass
    
if __name__ == '__main__':
    main()
        

    

