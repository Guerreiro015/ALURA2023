
#pip install mysql-connector-python
#pip install mysql.connector  

import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lucas0108',
    database='jogoteca'
)

cursor=conexao.cursor()
conexao.commit() # Quando edita/grava/deleta - banco de dados

#--------------------<>_______________________________________#
dados=('Romeu','romeu','123')
def inserir_usuarios(i):
        comando =f'INSERT INTO usuarios(nome,nickname,senha) VALUES("{i[0]}", "{i[1]}", "{i[2]}")'
        cursor.execute(comando)
        conexao.commit() # Quando edita/grava/deleta - banco de dados
#inserir_usuarios(dados)


def inserir_jogos(i):
        comando =f'INSERT INTO jogos(nome,categoria,console,ano,foto,obs) VALUES("{i[0]}", "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", "{i[5]}")'        
        cursor.execute(comando)
        conexao.commit() # Quando edita/grava/deleta - banco de dados
#inserir_jogos(dados)


def atualizar_usuarios(i):
    comando = f'UPDATE usuarios SET nome = "{i[0]}", nickname="{i[1]}", senha="{i[2]}" WHERE id = "{i[3]}" '
    cursor.execute(comando)
    conexao.commit() # Quando edita/grava/deleta - banco de dados
    
#atualizar_usuarios(dados,'Romeu')



def atualizar_jogos(i):
    comando = f'UPDATE jogos SET nome = "{i[0]}", categoria="{i[1]}", console="{i[2]}", ano="{i[3]}", foto="{i[4]}", obs="{i[5]}" WHERE id = "{i[6]}" ' 
    cursor.execute(comando) #nome,categoria,console,ano,foto,obs,id
    conexao.commit() # Quando edita/grava/deleta - banco de dados
    
#atualizar_jogos(dados,'ps5')
    
#     #DELETAR DADOS -----------------------------------------------------
busca='Faisca'
def excluir_usuario(i):    
    comando = f'DELETE FROM usuarios WHERE nome = "{i}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
#excluir_usuario(busca)

busca='Clash bandicoot'
def excluir_jogos(i):    
    comando = f'DELETE FROM jogos WHERE id = "{i}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
#excluir_jogos(busca)



    #VER inventário -----------------------------------------------------
def visualizar_usuarios():   
    comando=f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados    
    print (resultado)
    
#visualizar_usuarios()       
                
   

def visualizar_jogos():   
    comando=f'SELECT * FROM jogos'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados
   
    return resultado
#visualizar_jogos()        
            



#      con = lite.connect("INSS.bd")

# cursor=conexao.cursor()
# #ATUALIZAR DADOS -----------------------------------------------------
# def atualizar_dados(i):
#     with con:
#         cur = con.cursor()   
                
def ver_usuario(i): 
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lucas0108',
    database='jogoteca'
)

   
    with conexao:
        cursor=conexao.cursor()          
        comando=f'SELECT * FROM usuarios'
        cursor.execute(comando)
        resultado = cursor.fetchall() # ler banco de dados
        for row in resultado:
            if i in row:
                usuario=row[1]
                senha=row[3]
                log=(usuario,senha)                 
                break
            else:
                log='none'
        return log            
            
#ver_usuario('Romeu')
        
def ver_jogos(i): 
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lucas0108',
    database='jogoteca'
)
   
    with conexao:
        cursor=conexao.cursor()          
        comando=f'SELECT * FROM jogos'
        cursor.execute(comando)
        resultado = cursor.fetchall() # ler banco de dados
        lista=()
        for row in resultado:
            if i in row: 
                lista=(row,)             
                break
            else:
                lista=[]
        return lista          



# cursor.close()
# conexao.close()

            #excluir_jogos(('11',))


