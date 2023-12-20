import os
os.system('cls')

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
        
def finalizar_app():
    os.system('cls')
    print('Programa Finalizado')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')
    
# Trecho de código suprimido

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1:
           Cadastrar()
        elif opcao_escolhida == 2:
           listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def opcao_invalida():
    input('''Esta opção não é válida''')
        
    main()
lista_restaurante=["SUSHI",'SASHIMI']
def Cadastrar():
    os.system('cls')
    print( 'Cadastro de Restaurante')
    restaurante=input('Digite o Nome do Restaurante: ')
    lista_restaurante.append(restaurante)
    print( f'Restaurante --<< {restaurante}  >>--    cadastrado com Sucesso...')
    input ('Digite uma tecla para voltar ao menu principal.')
    main()

def listar_restaurante():
    print("LISTA DE RESTAURANTES ")

    for i in lista_restaurante:
        print(f'Restaurante {i} ')
    input ('Digite uma tecla para voltar ao menu principal.')
    main()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()