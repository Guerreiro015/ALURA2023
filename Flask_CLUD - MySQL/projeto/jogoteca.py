
from flask import Flask, render_template, request, redirect, session,flash,send_from_directory
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import mysql.connector
from dadosteca import *
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename



app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'

@app.route('/')
def login():
    usuario='Nenhum Usuário logado'
    return render_template('login.html',titulo='Fazer Login',usuario=usuario)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    nome=request.form['nome']
    senha=request.form['senha']
    usuario=request.form['nome']
    
    logar=ver_usuario(nome)
      
    if nome == logar[0] and senha == logar[1]:
         flash(f'Usuário {usuario} Logado com Sucesso!!')
         
         return redirect(url_for('index',usuario=usuario))
    else:
         flash('Não foi possível fazer Login!!')
         return redirect(url_for('login'))


@app.route('/index')
def index():     
    lista_jogos = visualizar_jogos()

    tit="Biblioteca de Jogos"
    return render_template('index.html',titulo=tit,jogos=lista_jogos)

@app.route('/editar_jogos/<int:id>')
def editar_jogos(id):    
    lista_jogos = ver_jogos(id)   
    tit=f"ALTERAR"
    return render_template('editar.html',jogos=lista_jogos,titulo=tit)

@app.route('/detalhes/<int:id>')
def detalhes(id):    
    lista_jogos = ver_jogos(id)   
    tit=f"DETALHES DO JOGO"
    return render_template('detalhes.html',jogos=lista_jogos,titulo=tit)


@app.route('/alterar_jogos', methods=['POST'])
def alterar_jogos(): 
    nome=request.form['nome']
    if nome=="":
       tit='ALTERAR'
       flash('Nenhum jogo para alterar!!')
       return render_template('index.html')
    else:
      id=request.form['id']        
      nome=request.form['nome']
      categoria=request.form['categoria']
      console=request.form['console']
      ano=request.form['ano']
      obs=request.form['obs']
      arquivo=request.files['arquivo']
      if not arquivo:
        foto=request.form['foto']      
      else:                 
        arquivo.save(f'projeto/uploads/{arquivo.filename}')
        foto=f'uploads/{arquivo.filename}' 

      lista=(nome,categoria,console,ano,foto,obs,id)

      print(lista)  
      atualizar_jogos(lista)
      flash(f'jogo  {nome} alterado!!')
      
      return redirect(url_for('index'))
    

@app.route('/deletar_jogos/<int:id>')
def deletar_jogos(id): 
      
      excluir_jogos(id)
      flash(f'jogo Deletado!!')
      
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
        detalhe=request.form['detalhe']
        arquivo=request.files['arquivo']
        arquivo.save(f'projeto/uploads/{arquivo.filename}')
        foto=f'uploads/{arquivo.filename}'
       

        novo_jogo = (nome,categoria,console,ano,foto,detalhe)
        inserir_jogos(novo_jogo)
        flash('Jogo adcionado com Sucesso!!')
        return redirect(url_for('index')) 
   
 
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)



@app.route('/logout')
def logout():    
    flash('Usuário Desconectado')
    return redirect(url_for('login'))



#app.run(debug=True)

    

  # trecho da app
app.run(host='0.0.0.0', port=8080)
