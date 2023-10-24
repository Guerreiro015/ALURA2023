from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
#pip install mysql-connector-python
#pip install mysql.connector  
import mysql.connector
import sys
import sqlite3 as lite

import os
os.system('cls')


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lucas@0108',
    database='jogoteca'
)
cursor=conexao.cursor()
conexao.commit() # Quando edita/grava/deleta - banco de dados




#READ
def visualizar_jogos():   
    comando=f'SELECT * FROM jogos'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados
   
    return resultado
#visualizar_jogos()        
            
        
                
def ver_usuario(i):           
        comando=f'SELECT * FROM jogos'
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

cursor.close()
conexao.close()

            #excluir_jogos(('11',))