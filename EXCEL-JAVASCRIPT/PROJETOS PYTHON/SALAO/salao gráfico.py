import os
os.system('cls')
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

Co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Azul
co4 = "#403d3d" # cinza
co5 = "#e06636" # laranja
co6 = "#038cfc" # Azul claro
co7 = "#3fbfb9" # Verde azulado
co8 = "#263238" # Preto claro
co9 = "#e9edf5" # Branco cinza claro
co10 = '#ffff00' # amarelo
co11 = '#ce0018' # Vermelho
co12 = '#106b21' # Verde
co13 = '#fc9303' # Laranja
co14 = '#5a005a' # roxo

import requests

import tkinter
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from datetime import timedelta
from datetime import *
from datetime import datetime
from dateutil import relativedelta

import requests
import sqlite3

conn = sqlite3.connect('salao.db')
global tree
global treev_lista

janela = tkinter.Tk()
janela.title('EMPRESA FICTÍCIA')
janela.geometry('1000x650')
janela.configure(background='#F0F8FF')
janela.resizable(width=FALSE, height=FALSE)
frame = tkinter.Frame(janela)
frame.pack()

style = ttk.Style(janela)
style.theme_use('clam')


#-------------------------------------------------------------------------------------------------
conn = sqlite3.connect('salao.db')
def visualizar():   
      lista_itens = []
      with conn:
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM salao_base")
        rows = cur.fetchall()
        for row in rows:
             lista_itens.append(row)
        return lista_itens
     
#----------------------------------------------------------------------

frame1 = tkinter.LabelFrame(frame,bg='bisque',fg='green',font='ivy 8 ')
frame1.grid(row=3,column=0,padx=10,pady=5)

def mostrar():
    global tree
    visualizar()
    tabela_head = ['INDICE','NOME','CPF','TELEFONE','E-MAIL','CADASTRO','CEP','RUA','NÚMERO','BAIRRO','CIDADE','UF',
                   'DDD','SERVIÇO','DATA SERVIÇO', 'Vlr. SERVICO','Quant. PARCELAS','Vlr. PARCELAS','% COMISSÃO','Vlr. COMISSÃO','FORMA DE PG']
    
    tree = ttk.Treeview(frame1, selectmode='extended',columns=tabela_head, show="headings",height=10)
    # ( tree é o nome da tabela) --------------------------

    # ajusta a largura da coluna para a string do cabeçalho
    for i in tabela_head:
        tree.column(i,anchor='center', width=43)
        tree.heading(i, text= i)

    # vertical scrollbar -- Barra de rolagem
    vsb = ttk.Scrollbar(frame1, orient="vertical", command=tree.yview)

    # horizontal scrollbar -- Barra de rolagem
    hsb = ttk.Scrollbar(frame1, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(row=0,column=1, sticky='ns')
    hsb.grid(row=1,column=0, sticky='ew')
    frame1.grid_rowconfigure(0, weight=5)
    frame1.grid_columnconfigure(0, weight=5)
    
    
  
    lista_itens = visualizar()
   # inserindo os itens dentro da tabela
        
    for item in lista_itens:
    
        tree.insert('', 'end', values=item)

mostrar()

frame2 = tkinter.LabelFrame(frame,bg='bisque',fg='green',font='ivy 8 ')
frame2.grid(row=3,column=0,padx=10,pady=5)


lista_itens = visualizar()
nomes=[]
valor=[]    
for item in lista_itens:
    nomes.append(item[1])
    valor.append(item[17])
print(nomes)
print(valor)  

df=pd.DataFrame({'NOMES': nomes,'VALOR': valor})
#df.set_index('NOMES', inplace=True)
print(df)


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

figura=plt.figure(figsize=(12,5),dpi=100)
ax = figura.add_subplot(111)


canvas = FigureCanvasTkAgg(figura, master = janela)   
canvas.draw() 
canvas.get_tk_widget().pack(expand = True) 

# canva = FigureCanvasTkAgg(figura,janela)
# canva.get_tk_widget().grid(row=1,column=0)


#fig,ax = plt.subplots(figsize=(14,5))
ax.bar(df['VALOR'], df['VALOR'],lw=3)


ax.set_title('GASTOS COM SERVIÇOS')
ax.set_xlabel('CLIENTES',fontsize=14,color='blue')
ax.set_ylabel('Comissões',fontsize=14)
ax.xaxis.set_tick_params(labelsize=8) #Tamanho da letra do eixo
ax.yaxis.set_tick_params(labelsize=10) #Tamanho da letra do eixo
plt.show()

janela.mainloop()