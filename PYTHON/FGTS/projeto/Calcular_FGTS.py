
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
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
import pandas as pd

tabela = pd.read_excel("BASE.xlsx",sheet_name="folha")

app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'


@app.route('/')   
def index():
    
    return render_template('index.html')


  
@app.route('/calcular', methods=['POST'])
def calcular():
 
    mes=(request.form['mes'])
    ano=(request.form['ano'])

    tb = pd.read_excel("conferencia_fgts.xlsx")

   
    return render_template('mostrar.html',dados=dados)

      
     
    
    

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
