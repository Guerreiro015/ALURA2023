



<<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>

<button type="button" class="btn btn-link">Link</button>


<a href="#" class="link-primary">Primary link</a></br>
<a href="#" class="link-secondary">Secondary link</a>
<a href="#" class="link-success">Success link</a>
<a href="#" class="link-danger">Danger link</a>
<a href="#" class="link-warning">Warning link</a>
<a href="#" class="link-info">Info link</a>
<a href="#" class="link-light">Light link</a>
<a href="#" class="link-dark">Dark link</a>

<a class="dropdown-item"  href="/index"> NOVO JOGO</a>
        <a class="dropdown-item"  href="/index">FAZER LOGIN</a>
        <a class="dropdown-item"  href="/index"> FAZER LOGOUT</a>
        <a class="dropdown-item"  href="/index">TESTE</a>

<body> 

              <font face="Arial"> Arial </font> <br />
              <font face="Courier"> Courier </font> <br />
              <font face="Georgia"> Georgia </font> <br />
              <font face="Helvetica"> Helvetica </font> <br />
              <font face="Times"> Times </font> <br />
              <font face="Tribuchet"> Trebuchet </font> <br />
              <font face="Verdana"> Verdana </font> <br />
                                        
              <font color="green"><br/>
              <font color="#FF0000"> Este texto e vermelho </font> <br />
              <font color="Yellow"> Esse e amarelo </font><body> <br />
              <font color="red"> Esse e verde </font><br />
              <font color="blue"> Esse e verde </font><br />
              <font color="green"> Esse e verde </font><br />
             </body>

             <body> 
              <font size="1" > Tamanho desta fonte:  1</font> <br />
              <font size="2" > Tamanho desta fonte:  2</font> <br />
              <font size="3"> Tamanho desta fonte:  3</font> <br />
              <font size="4"> Tamanho desta fonte:  4</font> <br />
              <font size="5"> Tamanho desta fonte:  5</font> <br />
              <font size="6"> Tamanho desta fonte:  6</font> <br />
              <font size="7"> Tamanho desta fonte:  7</font> <br />


           </body>


           <div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown button
  </button>
  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>
</div>


 
        <a href="/novo_jogo"> NOVO JOGO</a> <br/>
        <a href="/">FAZER LOGIN</a><br/>
        <a href="/logout"> FAZER LOGOUT</a><br/> 


colocar coisas no inicio ou final da página

 <div class="fixed-top">...</div>
<div class="fixed-bottom">...</div>


Posicionamento
Use estes utilitários de atalho, para definir o tipo de posicionamento de um elemento, rapidamente.

Valores comuns
Apesar de termos classes para definir o tipo de posicionamento, elas não são responsivas.

Copy
<div class="position-static">...</div>
<div class="position-relative">...</div>
<div class="position-absolute">...</div>
<div class="position-fixed">...</div>
<div class="position-sticky">...</div>



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