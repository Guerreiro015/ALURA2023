from loja import lojas 


portugal=lojas('Delicia','bacalhau')
japones=lojas('Susshi','Peixe')



portugal.receber_avaliacao('Gui', 8)
portugal.receber_avaliacao('Lais', 9)
portugal.receber_avaliacao('Emy', 7.9)
portugal.receber_avaliacao('Fran', 9.5)

japones.receber_avaliacao('Gui', 4)
japones.receber_avaliacao('Lais', 6)
japones.receber_avaliacao('Emy', 7.9)
japones.receber_avaliacao('Fran', 9.5)


def main():
  lojas.mostrar()

if __name__ == '__main__':
    main()
 