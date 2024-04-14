from loja import lojas 

suiço=lojas('suiça','internacional')
portugal=lojas('Delicia','bacalhau')
nordeste=lojas('rapadura','doce')


portugal.alternar()
nordeste.alternar()
print(nordeste)



def main():
  lojas.mostrar()

if __name__ == '__main__':
    main()
 