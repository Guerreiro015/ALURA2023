




#pip install mysql-connector-python
#pip install mysql.connector  
import os
os.system('cls')

import mysql.connector


#app = Flask(__name__) #instanciando Flask
  
#app.secret_key = 'alura'

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lucas@0108',
    database='jogoteca'

)

cursor=conexao.cursor()

conexao.commit() # Quando edita/grava/deleta - banco de dados


# #CREATE

# nom='romeu'
# nick='romeu'
# sen='123'
# comando =f'INSERT INTO usuarios(nome,nickname,senha) VALUES("{nom}", "{nick}", "{sen}")'
# cursor.execute(comando)
# conexao.commit() # Quando edita/grava/deleta - banco de dados


##--------------------<>--------------------------##


# nome="Genshi Impact"
# categoria="Mundo aberto"
# console="PC"
# ano="2021"

# comando =f'INSERT INTO jogos(nome,categoria,console,ano) VALUES("{nome}","{categoria}","{console}","{ano}")'
# cursor.execute(comando)
# conexao.commit() # Quando edita/grava/deleta - banco de dados



#UPDATE
# busca="RE6"
# nom="Gran Turismo 2"
# cat="Corrida"
# con="PS2"
# an="2019"

# comando = f'UPDATE jogos SET nome = "{nom}", categoria="{cat}", console="{con}", ano="{an}" WHERE nome = "{busca}" '
# cursor.execute(comando)
# conexao.commit() # Quando edita/grava/deleta - banco de dados


# DELETE
# busca = "RE3"
# comando = f'DELETE FROM jogos WHERE nome = "{busca}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados



#READ
comando=f'SELECT * FROM jogos'
cursor.execute(comando)
resultado = cursor.fetchall() # ler banco de dados

print(resultado)

##--------------------<>--------------------------##





cursor.close()
conexao.close()






#app.run(debug=True)

    

  # trecho da app
#app.run(host='0.0.0.0', port=8080)