def listra(): 
    print ("*"*50) 


listra()
print("* Bem vindo ao jogo de Adivinhação WHILE *".center(50))
listra()
tentativas=1     
while(tentativas !=0 ):
    num = 42
    chute = input("Digite o seu CHUTE ..:  ")
    chute = int(chute)
    if chute > 100 or chute < 0:
         continue # serve para retornar para inicio do while deste ponto


    if (chute == num):
            print('Você acertou na {}ª tentativa o numero é '.format(tentativas),chute)
            print("-"*50)
            print("Fim do jogo ".center(50))
            print("*"*50)
            tentativas=0

    elif (chute > num):
                print('\n {}ª tentativa errada - -  o número é menor que {}'.format(tentativas,chute))
                tentativas=tentativas+1
    elif (chute < num):
                print('\n {}ª tentativa errada - -  o número é maior que {}'.format(tentativas,chute))
                tentativas=tentativas+1
    else:
                print('erro desconhecido....')
