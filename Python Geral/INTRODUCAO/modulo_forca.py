def perdeu(x,y):
    
    print("=" * 50)
    print(f"INFELIZMENTE, voce NÃO acertou nas {x-1} tentativas \n")
    print(f"A palavra é - {y.upper()} -".center(50))
    print("=" * 50)


    print("  _______     ".center(50))
    print(" |/      |    ".center(50))
    print(" |    __(_)__ ".center(50))
    print(" |   ENFORCADO".center(50))
    print(" |            ".center(50))
    print(" |            ".center(50))
    print(" |            ".center(50))

    #print(" você foi enforcado! ".center(50))
    print("\n    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

    print("=" * 50)
    print("Fim do jogo".center(50))
    print("=" * 50)


def ganhou(tent,pala):
    print("=" * 50)
    print(f"PARABENS, voce acertou em {tent} tentativas".center(50))
    print(f"A palavra é - {pala.upper()} -".center(50))
    print("=" * 50)
               
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

    print("=" * 50)          
    print(" Fim do jogo".center(50))
    print("=" * 50)      

def enforcar(tentativa):
    tentativa = tentativa-1
    if(tentativa == 0):
        print("  _______     ")
        print(" |/           ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    
    if(tentativa == 1):
        print("  _______     ")
        print(" |/      |    ")
        print(" |           ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 2):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 3):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 4):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 5):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 6):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativa == 7):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativa == 8):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    if (tentativa == 9):
        print("  _______     ")
        print(" |/      |    ")
        print(" |    __(_)__ ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    
        
