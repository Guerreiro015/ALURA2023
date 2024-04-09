import os
os.system("cls")

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
#from criar_bd_inss_irrf import *
# imprtando os outros arquivos
import sys
import sqlite3 as lite
con = lite.connect("INSS.bd")


#ATUALIZAR DADOS -----------------------------------------------------
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = '''UPDATE dados SET 
                de1=?,ate1=?,ali1=?,par1=?,
                de2=?,ate2=?,ali2=?,par2=?,
                de3=?,ate3=?,ali3=?,par3=?,
                de4=?,ate4=?,ali4=?,par4=?,
                deir1=?,ateir1=?,aliir1=?,parir1=?,
                deir2=?,ateir2=?,aliir2=?,parir2=?,
                deir3=?,ateir3=?,aliir3=?,parir3=?,
                deir4=?,ateir4=?,aliir4=?,parir4=?,
                deir5=?,aliir5=?,parir5=?,tetoinss=?,
                dedudep=?,dedusimp=?'''
        
        cur.execute(query,i)
        con.commit()

def visualizar():   
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM dados")
        linha_dados = cur.fetchall()
        for i in linha_dados:
             lista_itens.append(i)
        return lista_itens
    #print(lista_itens)#
            


def inserir_dados(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO dados(de1,ate1,ali1,par1,de2,ate2,ali2,par2,de3,ate3,ali3,par3,de4,ate4,ali4,par4,deir1,ateir1,aliir1,parir1,deir2,ateir2,aliir2,parir2,deir3,ateir3,aliir3,parir3,deir4,ateir4,aliir4,parir4,deir5,aliir5,parir5,tetoinss,dedudep,dedusimp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                
                           
        cur.execute(query,i)
        con.commit()     





