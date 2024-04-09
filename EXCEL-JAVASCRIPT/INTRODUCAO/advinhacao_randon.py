def listra(): 
    print ("*"*50)
    print("* Bem vindo ao jogo de Adivinhação RANDOM *".center(50))
    print ("*"*50) 
listra()
import os
os.system('cls') or None

# # A funcao menu abaixo será usado como teste no programa advinhacao_menu
# def menu():
#     print("*"*50)
#     print("****  MENU DOS JOGOS DE ADVINHAR!  *****".center(50))
#     print("*"*50)


listra()

import random
num = round(random.random()*10)
num2 = round(random.randrange(101))
num3 = round(random.randrange(1,5))

tentativas=1     
while(tentativas !=0 ): 

    chute = input("Digite o seu CHUTE ..:  ")
    chute = int(chute)
    if chute > 100 or chute < 0:
         print(("Digite um nuero de 1 a 100") )
         continue# serve para retornar para inicio do while deste ponto


    if (chute == num):
            print("-"*50)
            print('Você acertou na {}ª tentativa o numero é '.format(tentativas),chute)
            print("-"*50)
            print("Fim do jogo ".center(50))
            print("*"*50,"\n")
            tentativas=0

    elif (chute > num):
                print('\n {}ª tentativa errada - -  o número é menor que {}'.format(tentativas,chute))
                input()
                os.system("cls") or None
                listra()
                tentativas=tentativas+1
    elif (chute < num):
                print('\n {}ª tentativa errada - -  o número é maior que {}'.format(tentativas,chute))
                input()
                os.system("cls") or None
                listra()
                tentativas=tentativas+1
    else:
                print('erro desconhecido....')

