from loja import lojas 


portugal=lojas('Delicia','bacalhau')

portugal.receber_avaliacao('Gui', 10)
portugal.receber_avaliacao('Lais', 10)
portugal.receber_avaliacao('Emy', 10)
portugal.receber_avaliacao('Fran', 10)



def main():
  lojas.mostrar()

if __name__ == '__main__':
    main()
 