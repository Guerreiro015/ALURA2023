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
    print(''' Programa Finalizado           
          '''
          
          )
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')
    
lista_restaurante=[ {'nome': 'SUSHI', 'categoria': 'japonesa', 'ativo': False},
                    {'nome': 'SASHINI', 'categoria': 'SASHIMI ', 'ativo': True},
                    {'nome': 'SAQUE', 'categoria': 'bebida  ', 'ativo': False}
                      ]

def voltar():
    input (' \nDigite uma tecla para voltar ao menu principal.')
    main()

def exibir_subtitulo(texto):
    linha="*" * (len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
               
        if opcao_escolhida == 1:
           Cadastrar()
        elif opcao_escolhida == 2:
           listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def opcao_invalida():
    input('''Esta opção não é válida''')        
    main()


def Cadastrar():
        # docstring
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes

    '''
        # docstring
   


    exibir_subtitulo('CADASTRO DE RESTAURNTES \n')
    
    restaurante=input('Digite o Nome do Restaurante: ')
    categoria=input(f'Digite a categoria do Restaurante {restaurante}: ')

    cadastro_restaurante={'nome': restaurante, 'categoria': categoria, 'ativo': False}

    lista_restaurante.append(cadastro_restaurante)

    print( f'Restaurante --<< {restaurante}  >>--    cadastrado com Sucesso...')
    voltar()


def listar_restaurante():
    exibir_subtitulo('LISTA DE RESTAUTANTES \n')

    nome_rest='RESTAURANTE'.upper()
    categ='Categoria'.upper()
    stat='Status'.upper()
    print(f'{nome_rest.ljust(20)} | {categ.ljust(20)} | {stat}')

    for i in lista_restaurante:
        nome=i['nome']
        categoria=i['categoria']
        ativo=i['ativo']
        print(f'{nome.ljust(23)}{categoria.ljust(23)}{ativo}')
    voltar()

def ativar_restaurante():
    exibir_subtitulo('ALTERNAR SITUAÇÃO DOS RESTAURANTE \n')
    restaurante=input('Digite o Nome do Restaurante para ativar: ')
    y=0
    for i in lista_restaurante:
        nome=i['nome']
        categoria=i['categoria']
        ativo=i['ativo']
        if restaurante==i['nome']:
          print(f' \nSituação anterior \nRestaurante: {nome}  <->  Categoria: {categoria} <-> Situação: {ativo}')
          i['ativo'] = not i['ativo']
          ativos=i['ativo']
          y=1
          if ativos==True:
              x="Ativado"
          else:
              x="Desativado"  
          print(f'\nSituação atual \nRestaurante: {nome}  <->  Categoria: {categoria} <-> Situação: {ativos}')
          print(f'\nO restaurante {nome} foi {x}:')
        #   USANDO OPERADOR TERNÁRIO
          print(f'O Restauarente {nome} está {x}') if x=='Ativado' else print(f'O Restauarente {nome} está Desativado')
        #   USANDO OPERADOR TERNÁRIO

    if y==0:
        print(f'\nO restaurante com nome de {restaurante.upper()} não está no nosso banco de dados')
        
    voltar()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()