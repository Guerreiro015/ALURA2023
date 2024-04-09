def forca():
    import modulo_titulo
    import random
    import modulo_palavra
    import modulo_forca
    import os

    os.system("cls") or None
    modulo_titulo.menu()

    # SELECIONANDO PALAVRA
   #============================================
    palavra = modulo_palavra.palavra_secreta()
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
          
            modulo_forca.perdeu(tentativa,palavra)

            fruta == lista  
            break

        os.system("cls") or None
        modulo_titulo.menu()
                     
        modulo_forca.enforcar(tentativa)
        
        print("LETRAS ACERTADAS =>  ", " ".join(lista))
        print("LETRAS CHUTADAS  =>  ", " ".join(digitada))
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
            
            modulo_forca.ganhou(tentativa,palavra)
            break  
        
        posicao = 0

   

if __name__ == "__main__":
  forca()
