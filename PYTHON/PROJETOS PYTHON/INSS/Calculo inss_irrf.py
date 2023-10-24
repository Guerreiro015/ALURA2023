import os
os.system("cls")
from base_inss import *
import sqlite3

#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas
# x = coluna
# y = Linha

# n, ne, e, se, s, sw, w, nw, or center
co0 = "#2e2d2b" # Preta
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


# Vamos ver algumas configurações de estilo mais comuns que podemos definir:
# Width – Largura do widget;
# Height – Altura do widget;
# Text – Texto a ser exibido no widget;
# Font – Família da fonte do texto;
# Fg – Cor do texto do widget;
# Bg – Cor de fundo do widget;
# Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.commondialog import Dialog
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
# importando os outros arquivos
from view_inss import *


# Criando janela------------------------------

janela = Tk()
janela.title("Encargos com folha de pagamento")
janela.geometry("1000x600")
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


frameCima = Frame(janela,width=1043, height=50, bg=co8, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

texto_cima= Label(frameCima, text='  CÁLCULO DE  ---   IRRF - INSS - FGTS', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)

frameMeio = Frame(janela,width=1043, height=330, bg=co7, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

framebaixo = Frame(janela,width=1043, height=303, bg=co3,pady=20, relief=FLAT)
framebaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)



l_salario = Label(frameMeio, text='  Valor do salário bruto', font=('verdana 10 bold'),bg=co7,fg=co1)
l_salario.place(x=0,y=0)
l_insalu = Label(frameMeio, text='  Insalubridade', font=('verdana 10 bold'),bg=co7,fg=co1)
l_insalu.place(x=0,y=25)
l_pericu = Label(frameMeio, text='  Periculosidade', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pericu.place(x=0,y=50)
l_he = Label(frameMeio, text='  Horas Extras ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_he.place(x=0,y=75)
l_adno = Label(frameMeio, text='  Adicional Noturno ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_adno.place(x=0,y=100)
l_dsr = Label(frameMeio, text='  DSR  - (H.E - Adic.Notur) ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_dsr.place(x=0,y=125)
l_outros = Label(frameMeio, text='  Outros Proventos  ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_outros.place(x=0,y=150)

meio_salario = Label(frameMeio, text=' DEDUÇÕES ', font=('verdana 13 bold'),bg=co7,fg=co8)
meio_salario.place(x=0,y=200)



l_falta=Label(frameMeio, text='  Valor das faltas', font=('verdana 10 bold'),bg=co7,fg=co1)
l_falta.place(x=0,y=225)
l_depe= Label(frameMeio, text='  Quant. de dependentes ', font=('verdana 10 bold'),bg=co7,fg=co1)
l_depe.place(x=0,y=250)
l_pensao= Label(frameMeio, text='  Pensão Alimentícia', font=('verdana 10 bold'),bg=co7,fg=co1)
l_pensao.place(x=0,y=275)

e_salario = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_salario.place(x=200,y=0)
e_insalu = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_insalu.place(x=200,y=25)
e_pericu = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_pericu.place(x=200,y=50)
e_he = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_he.place(x=200,y=75)
e_adno = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_adno.place(x=200,y=100)
e_dsr = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_dsr.place(x=200,y=125)
e_outros = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_outros.place(x=200,y=150)



e_faltas = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_faltas.place(x=200,y=225)

e_depe = Spinbox(frameMeio, from_=0, to=50)#***********#
e_depe.place(x=200,y=250)


e_pensao = Entry(frameMeio,width=20,justify=LEFT,relief=SOLID)
e_pensao.place(x=200,y=275)

imagem=Image.open("empresa.jpg")
imagem = imagem.resize((300,260))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frameMeio, image = imagem,bg=co1,fg=co4)
l_imagem.place(x=650,y=0)





global desc_inss,desc_irrf
def calculo():
 
  global desc_inss,desc_irrf,dedu_ir
  
  try:
    
    sal = 0 if e_salario.get() == '' else float(e_salario.get())
     
    ins = 0 if e_insalu.get() == '' else float(e_insalu.get())
     
    per = 0 if e_pericu.get() == '' else float(e_pericu.get())
     
    hex = 0  if e_he.get() == '' else float(e_he.get())
      
    adn = 0  if e_adno.get() == '' else  float(e_adno.get())
  
    ds = 0 if e_dsr.get() == '' else float(e_dsr.get())
          
    fal = 0 if e_faltas.get() == '' else float(e_faltas.get())
        
    pen = 0 if e_pensao.get() == '' else float(e_pensao.get())
       
    dep = 0 if e_depe.get() == '' else float(e_depe.get())
     
    out = 0 if e_outros.get() == '' else float(e_outros.get())
                
    total = (sal+ins+per+hex+adn+ds+out)-fal

    
    desc_inss = inss(total)

    dedu_ir=0
    dedu = 528
    dedu1=(desc_inss+pen+(dep*189.59))
    if dedu1 <= dedu:
      dedu_ir = dedu
    else:
      dedu_ir = dedu1

    ir = total-dedu_ir
      
    if ir<=0:
        ir=0
      
    print(f'Base de INSS R$: {total: .2f}')
    print(f'Base de IRRF R$: {ir: .2f}')
    print(f'Base de IRRF R$: {dedu: .2f}')
    print(f'Base de IRRF R$: {dedu1: .2f}')
    l_depe= Label(frameMeio, text=f'R$: {dep*dependente: ,.2f} ', font=('verdana 10 bold'),bg=co7,fg=co1)
    l_depe.place(x=340,y=250)    


    desc_irrf = irrf(ir,0)

    baixo_salario = Label(framebaixo, text=f'R$: {total: ,.2f}', width=15, font=('verdana 10 bold'),bg=co9,fg=co0)
    baixo_salario.place(x=200,y=0)
    baixo_salario = Label(framebaixo, text=f'R$: {desc_inss: ,.2f}',width=15, font=('verdana 10 bold'),bg=co9,fg=co0)
    baixo_salario.place(x=630,y=0)
      
    baixo_depe= Label(framebaixo, text=f'R$: {ir: ,.2f}', width=15, font=('verdana 10 bold'),bg=co9,fg=co0)
    baixo_depe.place(x=200,y=30)
    baixo_depe= Label(framebaixo, text=f'R$: {desc_irrf: ,.2f}', width=15,font=('verdana 10 bold'),bg=co9,fg=co0)
    baixo_depe.place(x=630,y=30)

    baixo_depe= Label(framebaixo, text=f'R$: {total: ,.2f}', width=15, font=('verdana 10 bold'),bg=co9,fg=co0)
    baixo_depe.place(x=200,y=60)
    baixo_depe= Label(framebaixo, text=f'R$: {total*8/100: ,.2f}',width=15, font=('verdana 10 bold'),bg=co9,fg=co0)
    baixo_depe.place(x=630,y=60)


    messagebox.showinfo('Sucesso', 'Cálculo executado com sucesso')

  except:
    messagebox.showerror('Erro', 'Por favor Verifique, A entrada de dados contém ERROS') 

def deletar():
   try:

    e_salario.delete(0, 'end')
    e_insalu.delete(0, 'end')
    e_pericu.delete(0, 'end')
    e_he.delete(0, 'end')
    e_adno.delete(0, 'end')
    e_dsr.delete(0, 'end')
    e_outros.delete(0, 'end')

    e_faltas.delete(0, 'end')
    e_depe.delete(0, 'end')
    e_pensao.delete(0, 'end')
    total =0

    messagebox.showinfo('Sucesso', 'Os dados foram limpos com sucesso')
 
    
   except IndexError:
    messagebox.showerror('Erro', 'Seleciona um dos dados na tabela') 

def tabelas():
  import tabela_inss
  
l_botao = Button(frameMeio,command=deletar,width=15,text="LIMPAR".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 12 bold"),bg=co12,fg=co1)
l_botao.place(x=350,y=0)
l_botao = Button(frameMeio,command=calculo,width=15,text="CALCULAR".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 12 bold"),bg=co11,fg=co1)
l_botao.place(x=350,y=60)
l_botao = Button(frameMeio,command=tabelas,width=15,text="VER TABELAS".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 12 bold"),bg=co10,fg=co4)
l_botao.place(x=350,y=120)

baixo_salario = Label(framebaixo, text='  BASE DO INSS.:', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_salario.place(x=0,y=0)
baixo_salario = Label(framebaixo, text='Valor de desconto INSS....:', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_salario.place(x=400,y=0)



baixo_faltas= Label(framebaixo, text='  BASE DO IRRF.:', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_faltas.place(x=0,y=30)
baixo_faltas= Label(framebaixo, text='Valor de desconto IRRF....: ', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_faltas.place(x=400,y=30)


baixo_depe= Label(framebaixo, text='  BASE DO FGTS:', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_depe.place(x=0,y=60)
baixo_depe= Label(framebaixo, text='Valor de depósito do FGTS:', font=('verdana 10 bold'),bg=co3,fg=co1)
baixo_depe.place(x=400,y=60)


            
   
janela.mainloop()