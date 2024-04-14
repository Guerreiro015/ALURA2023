from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
italiano = Restaurante('Pizza', 'Muzzarela')

suco=Bebida('caju',5.00,'Medio','Bom')
pao=Prato('Pãozinho',2.00,'Pão Fresquinho','Grande')
restaurante_praca.adicionar_no_cardapio(suco)
restaurante_praca.adicionar_no_cardapio(pao)

suco=Bebida('Borda',3.00,'Pequeno','Bom')
pao=Prato('A moda',10.00,'Muito Cara','Grande')
restaurante_praca.adicionar_no_cardapio(suco)
restaurante_praca.adicionar_no_cardapio(pao)


def main():
   
    restaurante_praca.exibir_cardapio

    # print(suco)
    # print(pao)

if __name__ == '__main__':
    main()