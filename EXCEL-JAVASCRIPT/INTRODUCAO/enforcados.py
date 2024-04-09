def forca():
    
    import random
    import os

    os.system("cls") or None

    

    
    menu()
    # SELECIONANDO PALAVRA
   #============================================
    palavra = palavra_secreta()
   #==============================================
    posicao = 0
    digitada = []
    #palavra = "abacaxi".upper()
    tamanho = len(palavra)
    lista = []

   

    for i in range(tamanho-1):  # adiconar _ na lista
        lista.append("_")


    tentativa = 0
    palavra = palavra.lower()  # Transformar em maisculos
    palavra = palavra.upper()  # Transformar em minúsculo
    palavra = palavra.strip()  # tira espaços no inicio e fim

    # palavra.index(item, inicio, fim) Para saber a posicao de um item dentro da lista

    # palavra = palavra.capitalize() # Primeira letra em maiúscula

    # A funcao " ".join serve para imprimir um lista sem os colchetes

    # A função .count() contar o número de ocorrências de um determinado elemento em uma lista.

    fruta = list(palavra)
    print(" ".join(fruta), tamanho)

    while fruta != lista:
        tentativa += 1

        if tentativa > 10:
          
            perdeu(tentativa,palavra)
            input("FIM DO JOGO")

            fruta == lista  
            break

        os.system("cls") or None
        menu()
                     
        enforcar(tentativa)
        
        print("\33[1;34m LETRAS ACERTADAS =>  ", " ".join(lista))
        print("\33[1;33m LETRAS CHUTADAS  =>  ", " ".join(digitada))
        print("\nAcerte a palavra acima...")
        print("-" * 50)
        chute = input(f"{tentativa}ª Tentativa,  Qual o seu chute? ")
        print("-" * 50)
        chute = chute.strip().upper()
        digitada.append(chute)

        if chute not in (fruta):
            print(f"A letra digitada, não tem na palavra secreta")
            input("")
            continue

        for letra in palavra:
            if chute.upper() == letra.upper():
                lista[posicao] = chute
                print(f" A letra  digitada foi encontrada na posição ( {posicao} )")
                print(" ".join(lista))
                input("")
                posicao += 1

            else:
                posicao += 1
        if fruta == lista:
            
            ganhou(tentativa,palavra)
            input("FIM DO JOGO")
            break  
        
        posicao = 0
def palavra_secreta():
        with open("lista_frutas.txt","w") as arquivo:
            arquivo.write("groselha\nbanana\nmelancia\nmanga\nabacaxi\nmaracuja\nmorango\nameixa\ngoiaba\ncaju\npera\ncarambola\nlaranja\ncaqui\nabacate\nmamao\n")

        import random
        with open("lista_frutas.txt","r") as lista:
            ler = lista.readlines()
        tamanho = len(ler)
        numero = random.randrange(0,tamanho)

        palavra = ler[numero]
        return palavra


def menu():
        print("*" * 50)
        print("JOGO DA FORCA".center(50))
        print("=" * 50)
        print("*  Você terá 10 tentativas, depois ...  *".center(50))
        print("-" * 50)


def perdeu(x,y):
    
    print("=" * 50)
    print(f"\033[1,31 INFELIZMENTE, voce NÃO acertou nas {x-1} tentativas \n")
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
    
   

if __name__ == "__main__":
  forca()
