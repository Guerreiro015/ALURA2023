
from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3



from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd

import sys
import sqlite3 as lite
con = sqlite3.connect("jogoteca.db",check_same_thread=False)

dados = ['romeu','romeu','123']
novos_dados = ['Tomb Raider','Aventura','Ps1000','2050']


    #Criar tabela usuarios------------------------------------------------
def criar_usuario():
        with con:
            cur = con.cursor()
            cur.execute ("CREATE TABLE IF NOT EXISTS usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome, nickname,senha)" )    

    #criar_usuario()

    #Criar tabela usuarios------------------------------------------------
def criar_jogos():
        with con:
            cur = con.cursor()
            cur.execute( "CREATE TABLE IF NOT EXISTS jogos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome,categoria,console,ano)")
            
    #criar_jogos()


def inserir_usuario(i):
        with con:
            cur = con.cursor()
            query = "INSERT INTO usuario(nome, nickname,senha) VALUES(?,?,?)"
            cur.execute(query,i)
    #inserir_usuario(dados)

def inserir_jogos(i):
        with con:
            cur = con.cursor()
            query = "INSERT INTO jogos(nome,categoria,console,ano) VALUES(?,?,?,?)"
            cur.execute(query,i)
#inserir_jogos(novos_dados)  



    #ATUALIZAR DADOS -----------------------------------------------------
def atualizar_usuario(i):
        with con:
            cur = con.cursor()
            query = '''UPDATE usuario SET nome=?, nickname=?, senha = ? WHERE id=?'''
            cur.execute(query,i)

def atualizar_jogos(i):
        with con:
            cur = con.cursor()
            query = '''UPDATE jogos SET nome=?, categoria=?, console=?, ano=? WHERE id=?'''
            cur.execute(query,i)
    
    #DELETAR DADOS -----------------------------------------------------



    #VER inventário -----------------------------------------------------
def visualizar_usuario():   
        lista_itens = []
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuario")
            rows = cur.fetchall()

            for row in rows:
                lista_itens.append(row)
            
            return lista_itens
            #print(lista_itens)
        
                
    #visualizar_usuario()  

def visualizar_jogos():   
        lista_itens = []
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM jogos")
            rows = cur.fetchall()

            for row in rows:
                lista_itens.append(row)
            
            return lista_itens
            #print(lista_itens)
  
#visualizar_jogos()        
            
        
                
def ver_usuario(i):   
        lista_itens = []
        with con:
            usuario='none'
            cur = con.cursor()
            cur.execute("SELECT * FROM usuario")
            rows = cur.fetchall()
            for row in rows:
                if i in row:
                    usuario=row[1]
                    senha=row[3]
                    log=(usuario,senha)
                    break
                else:
                    log='none'
            
            return log
        
def ver_jogos(i):   
        lista = []
        with con:           
            cur = con.cursor()
            cur.execute("SELECT * FROM jogos")
            rows = cur.fetchall()
            for row in rows:
                if i in row:
                   id=row[0]
                   nome=row[1]
                   categoria=row[2]
                   console=row[3]
                   ano=row[4]
                   lista=(id,nome,categoria,console,ano)
                   lista=[lista]
                   break
                                 
            return lista

def excluir_usuario(i):
        with con:
            cur = con.cursor()
            query = "DELETE FROM usuario WHERE id=?"
            cur.execute(query, i)
    #deletar_usuario('6')  

def excluir_jogos(i):
        with con:
            cur = con.cursor()
            query = "DELETE FROM jogos WHERE id=?"
            cur.execute(query, i)


            #excluir_jogos(('11',))


