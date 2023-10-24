
from flask import Flask, render_template, request, redirect, session,flash,send_from_directory
import mysql
from datetime import *
import time
import sqlite3
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pyodbc
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
#pip install PyMySQL


engine = ce('mysql://root:lucas0108@localhost:3306/jogoteca')
base=declarative_base()
session=sessionmaker(bind=engine)
session=session()


class usuarios(base):
   __tablename__= "usuarios"

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(45), nullable=False)
   nickname = Column(String(45), nullable=False)
   senha = Column(String(45), nullable=False)
   
class jogos(base):
   __tablename__= "jogos"

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(45), nullable=False)
   categoria = Column(String(45), nullable=False)
   console = Column(String(45), nullable=False)   
   ano = Column(String(45), nullable=False)   
   foto = Column(String(45), nullable=False)   
   obs = Column(String(200), nullable=False)   
   





app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'


@app.route('/')
def login():    
    return render_template('login.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/cadastro_usuarios')
def cadastro_usuarios():    
    return render_template('cadastro_usuarios.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nome=request.form['nome']
    senha=request.form['senha']
    usuario=request.form['nome']
    
    dados=session.query(usuarios).all()
      
    if nome == dados[0].nome and senha == dados[0].senha:
         
         flash(f'Usuário {usuario} Logado com Sucesso!!')
         
         return redirect(url_for('index',usuario=usuario))
    else:
         flash('Não foi possível fazer Login!!')
         return render_template('login.html')
    
#---------------------------------------------<>--------------------------------------------------    

@app.route('/autenticar_cadastro', methods=['POST'])
def autenticar_cadastro():
    nome=request.form['nome']
    nickname=request.form['nickname']
    senha=request.form['senha']
    senha2=request.form['senha2']

    usuario=request.form['nome']
    dados=session.query(usuarios).all()

    if nome == "" or nickname =="" or senha =="":
        flash('Preencha todos os campos!!')
        return render_template('cadastro_usuarios.html')

    if nome in dados[0].nome:            
        flash('Usuario já Existe!!')
        return render_template('cadastro_usuarios.html')

    if senha != senha2:
        flash('Senhas não conferem, tente colocar senhas iguais!!')
        return render_template('cadastro_usuarios.html')
    
    
    else:        
        flash(f'Usuário {usuario} cadastrado com Sucesso!!')            
        return redirect(url_for('login',usuario=usuario))
    #---------------------------------------------<>--------------------------------------------------     

@app.route('/index')
def index():
    dados=session.query(jogos).all()     
    lista_jogos = dados

    tit="Biblioteca de Jogos"
    return render_template('index.html',titulo=tit,jogos=lista_jogos)

#---------------------------------------------<>--------------------------------------------------   


@app.route('/usuario')
def usuario():
    dados=session.query(usuarios).all()     
    lista_usuarios = dados

    tit="USUARIOS"
    return render_template('usuarios.html',titulo=tit,usuarios=lista_usuarios)

#---------------------------------------------<>--------------------------------------------------   

@app.route('/editar_jogos/<int:id>')
def editar_jogos(id):
    dados=session.query(jogos).filter(jogos.id==id)   
    tit=f"ALTERAR"
    return render_template('editar.html',jogos=dados,titulo=tit)
#---------------------------------------------<>--------------------------------------------------   

@app.route('/detalhes/<int:id>')
def detalhes(id):  
    dados=session.query(jogos).filter(jogos.id==id)  
    tit=f"DETALHES DO JOGO"
    return render_template('detalhes.html',jogos=dados,titulo=tit)

#---------------------------------------------<>--------------------------------------------------   

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
      timestamp=time.time()
      arquivo=request.files['arquivo']
      if not arquivo:
        foto=request.form['foto']      
      else:                 
        arquivo.save(f'projeto/uploads/{arquivo.filename}-{timestamp}')
        foto=f'uploads/{arquivo.filename}-{timestamp}' 

      session.query(jogos).filter(jogos.id==id).update({'nome': nome,'categoria': categoria,'console': console,'ano': ano,'foto':foto,'obs': obs })
      session.commit()  
      
      flash(f'jogo  {nome} alterado!!')
      
      return redirect(url_for('index'))
    
#---------------------------------------------<>--------------------------------------------------   

@app.route('/deletar_jogos/<int:id>')
def deletar_jogos(id): 
      
      session.query(jogos).filter(jogos.id==id).delete()
      session.commit() 
      flash(f'Jogo Deletado !!')
      return redirect(url_for('index'))
    

#---------------------------------------------<>--------------------------------------------------   

@app.route('/novo_jogo')
def novo_jogo():
    return render_template('novo_jogo.html', titulo="novo jogo")

#---------------------------------------------<>--------------------------------------------------   

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
        obs=request.form['obs']
        timestamp=time.time()
        arquivo=request.files['arquivo']
        arquivo.save(f'projeto/uploads/{arquivo.filename}-{timestamp}')
        foto=f'uploads/{arquivo.filename}-{timestamp}'
               
        dados=jogos(nome=nome, categoria=categoria, console=console, ano=ano, foto=foto, obs=obs) #instanciando
        session.add(dados) #inserindo
        session.commit() # gravando
        flash('Jogo adcionado com Sucesso!!')
        return redirect(url_for('index')) 
   
#---------------------------------------------<>--------------------------------------------------   

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

#---------------------------------------------<>--------------------------------------------------   

@app.route('/logout')
def logout():    
    flash('Usuário Desconectado')
    return redirect(url_for('login'))

#---------------------------------------------<>--------------------------------------------------   


session.close()  

app.run(debug=True)
#app.run(host='0.0.0.0', port=8080)
