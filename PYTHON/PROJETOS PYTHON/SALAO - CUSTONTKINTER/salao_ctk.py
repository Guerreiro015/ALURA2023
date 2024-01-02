import os
os.system('cls')

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
#from dateutil import relativedelta
import customtkinter
import customtkinter as ctk
import tkinter as tk

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()



import requests
import sqlite3

conn = sqlite3.connect('salao.db')
global tree
global treev_lista

janela = customtkinter.CTk()
janela.title('EMPRESA FICTÍCIA')
janela.geometry('1000x650')
janela.configure(background='#F0F8FF')
janela.resizable(width=FALSE, height=FALSE)
frame = tkinter.Frame(janela)
frame.pack()

# style = ttk.Style(janela)
# # style.theme_use('clam')
customtkinter.set_default_color_theme("dark-blue")

janela1 = tkinter.LabelFrame(frame, text = 'Informações de Login',font=' ivy 10 bold')
janela1.grid(row=0,column=0,padx=10,pady=5)

janela2 = tkinter.LabelFrame(frame, text = 'Informações do Cliente',font=' ivy 10 bold')
janela2.grid(row=1,column=0,padx=10,pady=5)

janela3 = tkinter.LabelFrame(frame, text = 'confirmação'.upper(),font=' ivy 10 bold')
janela3.grid(row=2,column=0,padx=10,pady=5)

texto = ctk.CTkLabel(janela1, text="Fazer Login")
texto.grid(row=0,column=0,padx=10,pady=5)
email = ctk.CTkEntry(janela1, placeholder_text="Seu e-mail")
email.grid(row=1,column=0,padx=10,pady=5)
senha = ctk.CTkEntry(janela1, placeholder_text="Sua senha", show="*")
senha.grid(row=1,column=1,padx=10,pady=5)
nome_label = ctk.CTkLabel(janela2,text='Nome do Cliente')
nome_label.grid(row=0,column=0,padx=10,pady=5)
nome1 = ctk.CTkEntry(janela2, placeholder_text="Nome cliente")
nome1.grid(row=1,column=0,padx=10,pady=5)
tel = ctk.CTkEntry(janela2, placeholder_text="Teçefone do cliente")
tel.grid(row=1,column=1,padx=10,pady=5)

tel = ctk.CTkButton(janela3,text="confirme os dados".upper())
tel.grid(row=0,column=1,padx=10,pady=5)



janela.mainloop()

