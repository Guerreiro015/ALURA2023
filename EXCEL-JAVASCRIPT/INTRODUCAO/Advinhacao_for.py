def listra():
    print("*" * 50)
    print("* Bem vindo ao jogo de Adivinhação *".center(50))
    print("*" * 50)


import os

os.system("cls") or None
listra()

num = 42
chance = 1
for i in range(chance, 10):
    chute = input("Digite o seu CHUTE ..:  ")
    chute = int(chute)
    if chute == num:
        print("-" * 50)
        print("Você acertou, na chance {}, o numero é ".format(chance), chute)
        print("-" * 50)

        print("Fim do jogo ".center(50))
        print("-" * 50)
        break

    elif chute > num:
        print(
            "\n A Chance {}, chute {} Não deu, você errou - -  o número é MENOR\n".format(
                chance, chute
            )
        )
        input()
        os.system("cls") or None
        listra()
        chance = chance + 1

    elif chute < num:
        print(
            "\n A Chance {}, chute {} Não deu, você errou - -  o número é MAIOR\n".format(
                chance, chute
            )
        )
        input()
        os.system("cls") or None
        listra()
        chance = chance + 1
        chance = chance + 1

    else:
        print("erro desconhecido....")
