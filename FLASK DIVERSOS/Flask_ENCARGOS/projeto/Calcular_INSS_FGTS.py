
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
from bases_2023 import *
#pip install PyMySQL


engine = ce('mysql://root:lucas0108@localhost:3306/base')
bases=declarative_base()
session=sessionmaker(bind=engine)
session=session()


class usuarios(bases):
   __tablename__= "usuarios"

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(45), nullable=False)
   email = Column(String(45), nullable=False)
   empresa = Column(String(45), nullable=False)
   senha = Column(String(45), nullable=False)



app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'


@app.route('/')   
def index():
    dados=session.query(usuarios).all()         

    tit="imposto de renda"
    return render_template('index.html',titulo=tit,dados=dados)


@app.route('/login')
def login():    
    return render_template('login.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/cadastro_usuarios')
def cadastro_usuarios():    
    return render_template('cadastro_usuarios.html')

#---------------------------------------------<>--------------------------------------------------   
#---------------------------------------------<>--------------------------------------------------   

@app.route('/calculo_inss')
def calculo_inss():    
    return render_template('calculo_inss.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nome=request.form['nome']    
    senha=request.form['senha']
    usuario=request.form['nome']
    
    dados=session.query(usuarios).all()
    x=0
    for dado in dados:            
       if nome == dado.nome and senha == dado.senha: 
          x=0        
          flash(f'Usuário {usuario} Logado com Sucesso!!')         
          return redirect(url_for('index',dados=dados))           
       else: 
          x +=1           
    if x > 0:
         flash('Não foi possível fazer Login!!')
         return render_template('login.html')
    
#---------------------------------------------<>--------------------------------------------------    

@app.route('/autenticar_cadastro', methods=['POST'])
def autenticar_cadastro():
    nome=request.form['nome']
    email=request.form['email']
    empresa=request.form['empresa']
    senha=request.form['senha']
    senha2=request.form['senha2']

    usuario=request.form['nome']
    dados=session.query(usuarios).all()

    if nome == "" or email == "" or senha == "" or email == "":
        flash('Preencha todos os campos!!')
        return render_template('cadastro_usuarios.html')
    
    if not "@" in email or not ".com" in email:
        flash('E-mail digitado não é válido!!')
        return render_template('cadastro_usuarios.html')

    if nome in dados[0].nome:            
        flash('Usuario já Existe!!')
        return render_template('cadastro_usuarios.html')

    if senha != senha2:
        flash('Senhas não conferem, tente colocar senhas iguais!!')
        return render_template('cadastro_usuarios.html')
    
    
    else:        
        flash(f'Usuário {usuario} cadastrado com Sucesso!!')            
        dados=usuarios(nome=nome, email=email, empresa=empresa, senha=senha) #instanciando
        session.add(dados) #inserindo
        session.commit() # gravando
        flash('Jogo adcionado com Sucesso!!')      
        return redirect(url_for('login',usuario=usuario))
    


#---------------------------------------------<>--------------------------------------------------   
@app.route('/calcular_inss', methods=['POST'])
def calcular_inss():
 
    salbase=float(request.form['salbase'])
    diastrab=float(request.form['diastrab'])
    hr50=float(request.form['hr50'])
    hr100=float(request.form['hr100'])
    adcnot=float(request.form['adcnot'])
    falta=float(request.form['falta'])
    dsr=float(request.form['dsr'])
    atrasos=float(request.form['atrasos'])
    depsf=float(request.form['depsf'])
    depir=float(request.form['depir'])
    opperic=(request.form['opperic'])
    opinsal=(request.form['opinsal'])
    insal=float(request.form['insal'])
    pensao=round(float(request.form['pensao']),2)
    salariominimo=1320
    salariofamilia=59.82
    tetosalariofailia=1754.18
    valorsalfam=round(depsf*salariofamilia,2)
    
    valordep=round(depir*189.59,2)
    deducaosimplificada=528
    
    if opinsal == 'sim':
        valor_insal=round((salariominimo*insal)/100,2)
    else: valor_insal=0

    if opperic == "sim" and opinsal == "nao":
        valor_peric=round((salbase*30/100),2)
    else: valor_peric = 0

    valorhora=salbase/220
    valorhora50=valorhora*1.5
    valorhora100=valorhora*2
    valoradcnot=valorhora*0.2
    

    valordia=salbase/30

    salario=round(valordia*diastrab,2)    
    horas50=round(hr50*valorhora50,2)
    horas100=round(hr100*valorhora100,2)
    adcnotur=round(adcnot*valoradcnot,2)
    somahoad = (horas100+horas50+adcnot)
    dsrhoad=round((somahoad)/25*5,2)

    valorfaltas=round(valordia*falta,2)
    valordsr=round(valordia*dsr,2)
    valoratrasos=round(valorhora*atrasos,2)

    bruto=round(salario + horas50 + horas100 + adcnotur+valor_insal+valor_peric+dsrhoad ,2)
    if bruto <= tetosalariofailia:       
        bruto += valorsalfam
    else:
        valorsalfam=0    
    descontos=round(valorfaltas+valordsr+valoratrasos,2)
    desc=round(valorfaltas+valordsr+valoratrasos+pensao,2)
    
    baseinss=round(bruto-descontos,2)
    basefgts=baseinss

    valorinss=round(inss(baseinss),2)
    if (valorinss+pensao+valordep) <= deducaosimplificada:
        descir=deducaosimplificada
    else:
        descir=(valorinss+pensao+valordep)

    baseir=round(baseinss-descir,2)
    if baseir <=0:
        baseir=0        

    valorirrf=round(irrf(baseir),2)
       
    valorfgts=baseinss*0.08
    valorfgts=round(valorfgts,2)
    
    dados={ 'desc': desc, 'dsrhoad': dsrhoad, 'salario': f'{salario: ,.2f}', 'bruto': f'{bruto: ,.2f}', 'insal': f'{valor_insal: ,.2f}', 'peric': f'{valor_peric: ,.2f}', 'valorsf': valorsalfam, 'valorhe50': horas50, 'valorhe100': horas100,'valoradcnot': adcnotur, 'valordsr': valordsr,'Faltas': valorfaltas,'Atrasos':valoratrasos,'baseinss': f'{baseinss: ,.2f}','valorinss':valorinss,'basefgts': f'{basefgts: ,.2f}','valorfgts': f'{valorfgts: .2f}', 'baseir':f'{baseir: ,.2f}', 'valorir':valorirrf,'valordep':valordep, 'pensao': pensao}

    print(valoratrasos)
    return render_template('mostrar_inss.html',dados=dados)       

#---------------------------------------------<>--------------------------------------------------   
#---------------------------------------------<>--------------------------------------------------   
@app.route('/encargos')
def encargos():
   return render_template('encargos_trabalhista.html')  




#---------------------------------------------<>--------------------------------------------------   
#---------------------------------------------<>--------------------------------------------------   

@app.route('/logout')
def logout():    
    flash('Usuário Desconectado')
    return redirect(url_for('login'))

#---------------------------------------------<>--------------------------------------------------   


session.close()  

app.run(debug=True)
#app.run(host='0.0.0.0', port=8080)
