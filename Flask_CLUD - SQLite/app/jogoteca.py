
from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
from dadosteca import *



app = Flask(__name__) #instanciando Flask
  

app.secret_key = 'alura'

  

@app.route('/')
def login():
    usuario='Nenhum Usuário logado'
    return render_template('login.html',titulo='Fazer Login',usuario=usuario)


@app.route('/index')
def index():     
    lista_jogos = visualizar_jogos()

    tit="Biblioteca de Jogos"
    return render_template('index.html',titulo=tit,jogos=lista_jogos)

@app.route('/buscar_jogos', methods=['POST'])
def buscar_jogos(): 
    buscar=request.form['busca'] 
    lista_jogos = ver_jogos(buscar)
    if lista_jogos==[]:
       flash('Jogo nao encontrado!!')
       tit="Não Encontrado"
       return render_template('index.html',jogos=lista_jogos,titulo=tit)
    else:
       tit=f"Jogo Encontrado {buscar}"
       return render_template('buscar.html',jogos=lista_jogos,titulo=tit)

@app.route('/alterar_jogos', methods=['POST'])
def alterar_jogos(): 
    nome=request.form['nome']
    if nome=="":
       tit='ALTERAR'
       flash('Nenhum jogo para alterar!!')
       return render_template('index.html')
    else:
      nome=request.form['nome']
      categoria=request.form['categoria']
      console=request.form['console']
      ano=request.form['ano']
      id=request.form['id']

      lista=(nome,categoria,console,ano,id)

      print(lista)  
      atualizar_jogos(lista)
      flash(f'jogo  {nome} alterado!!')
      
      return redirect(url_for('index'))
    

@app.route('/deletar_jogos', methods=['POST'])
def deletar_jogos(): 
    nome=request.form['nome']    
    if nome=="":
       
       flash('Nenhum jogo para DELETAR!!')
       return render_template('index.html')
    else:
     
      id=request.form['id']

      lista=(str(id))

      print(lista)  
      excluir_jogos((lista,)) #Transformando em tupla
      flash(f'jogo  {nome} Deletado!!')
      
      return redirect(url_for('index'))
    


@app.route('/novo_jogo')
def novo_jogo():
    return render_template('novo_jogo.html', titulo="novo jogo")


@app.route('/criar', methods=['POST'])
def criar():    
    nome=request.form['nome']
    if nome == "":
        flash('Não foi posível cadastrar jogo - Dados insuficienntes - ')
        return render_template('novo_jogo.html', titulo="novo jogo")
    else:
        nome=request.form['nome']
        categoria=request.form['categoria']
        console=request.form['console']
        ano=request.form['ano']
       

        novo_jogo = (nome,categoria,console,ano)
        inserir_jogos(novo_jogo)
        flash('Jogo adcionado com Sucesso!!')
        return redirect(url_for('index'))
 
   

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nome=request.form['nome']
    senha=request.form['senha']
    usuario=request.form['nome']

    ver_usuario(nome)
    logar=ver_usuario(nome)
      
    if nome == logar[0] and senha == logar[1]:
         flash(f'Usuário {usuario} Logado com Sucesso!!')
         
         return redirect(url_for('index',usuario=usuario))
    else:
         flash('Não foi possível fazer Login!!')
         return redirect(url_for('login'))

  
    
@app.route('/logout')
def logout():    
    flash('Usuário Desconectado')
    return redirect(url_for('login'))




app.run(debug=True)

    

  # trecho da app
#app.run(host='0.0.0.0', port=8080)
