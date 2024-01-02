from loja import lojas 


portugal=lojas('Delicia','bacalhau')
japones=lojas('Susshi','Peixe')
frances=lojas('Soboro Dontê','lanches')


japones.alternar()

portugal.receber_avaliacao('Gui', 8)
portugal.receber_avaliacao('Lais', 8.4)
portugal.receber_avaliacao('Emy', 7.1)
portugal.receber_avaliacao('Fran', 9.5)

japones.receber_avaliacao('Gui', 7)
japones.receber_avaliacao('Lais', 9)
japones.receber_avaliacao('Emy', 5)
japones.receber_avaliacao('Fran',4)


def main():
  lojas.mostrar()

if __name__ == '__main__':
    main()
 