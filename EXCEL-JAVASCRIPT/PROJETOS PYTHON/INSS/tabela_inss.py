import os
os.system("cls")

#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas
# x = coluna
# y = Linha

# Vamos ver algumas configurações de estilo mais comuns que podemos definir:
# Width – Largura do widget;
# Height – Altura do widget;
# Text – Texto a ser exibido no widget;
# Font – Família da fonte do texto;
# Fg – Cor do texto do widget;
# Bg – Cor de fundo do widget;
# Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).

# n, ne, e, se, s, sw, w, nw, or center
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
#from criar_bd_inss_irrf import *



# Criando janela------------------------------

janela = Tk()
janela.title("Encargos com folha de pagamento")
janela.geometry("1000x600")
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


frameCima = Frame(janela,width=1043, height=30, bg=co8, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

texto_cima= Label(frameCima, text='  TABELAS DE IMPOSTO DE RENDAS e INSS ', width=600, compound=CENTER, relief=RAISED, anchor=SW, font=('verdana 15 bold'),bg=co9,fg=co2)
texto_cima.place(x=0,y=0)

frameMeio = Frame(janela,width=1043, height=250, bg=co2, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

framebaixo = Frame(janela,width=1043, height=330, bg=co3,pady=20, relief=FLAT)
framebaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)



l_salario = Label(frameMeio, text='  TABELA DE INSS  ', font=('verdana 13 bold'),bg=co3,fg=co1)
l_salario.place(x=600,y=0)
l_insalu = Label(frameMeio, text=' Digite abaixo os dados para alteração da tabela ', font=('verdana 11 bold'),bg=co3,fg=co1)
l_insalu.place(x=30,y=10)

lista_itens=visualizar()    
def tabelas_atuais():
  lista_itens=visualizar()    

  base_de1=lista_itens[0][1]
  base_de2=lista_itens[0][5]
  base_de3=lista_itens[0][9]
  base_de4=lista_itens[0][13]
  base_ate1=lista_itens[0][2]
  base_ate2=lista_itens[0][6]
  base_ate3=lista_itens[0][10]
  base_ate4=lista_itens[0][14]
  inssali1 = lista_itens[0][3]
  inssali2 = lista_itens[0][7]
  inssali3 = lista_itens[0][11]
  inssali4 = lista_itens[0][15]
  dedu1 = lista_itens[0][4]
  dedu2 = lista_itens[0][8]
  dedu3 = lista_itens[0][12]
  dedu4 = lista_itens[0][16]

  base_deir1=lista_itens[0][17]
  base_deir2=lista_itens[0][21]
  base_deir3=lista_itens[0][25]
  base_deir4=lista_itens[0][29]
  base_deir5=lista_itens[0][33]


  base_ateir1=lista_itens[0][18]
  base_ateir2=lista_itens[0][22]
  base_ateir3=lista_itens[0][26]
  base_ateir4=lista_itens[0][30]
  base_ateir5=100000000

  irraliir1 = lista_itens[0][19]
  irraliir2 = lista_itens[0][23]
  irraliir3 = lista_itens[0][27]
  irraliir4 = lista_itens[0][31]
  irraliir5 = lista_itens[0][34]


  deduir1 = lista_itens[0][20]
  deduir2 = lista_itens[0][24]
  deduir3 = lista_itens[0][28]
  deduir4 = lista_itens[0][32]
  deduir5 = lista_itens[0][35]

  teto_inss = lista_itens[0][36]
  dependente = lista_itens[0][37]
  deducao_simplicada = lista_itens[0][38]

  l_texto_titulo = Label(frameMeio, text=f'    Alíquota           Dedução ', font=('verdana 8 bold'),bg=co3,fg=co1)
  l_texto_titulo.place(x=720,y=50)
  l_texto_titulo = Label(frameMeio, text=f'R$: {base_de1: ,.2F}            até       R$: {base_ate1: ,.2F}                    {inssali1: ,.2f}%                R$: {dedu1: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
  l_texto_titulo.place(x=490,y=70)
  l_texto_titulo = Label(frameMeio, text=f'R$: {base_de2: ,.2F}    até       R$: {base_ate2: ,.2F}                    {inssali2:,.2f}%                 R$: {dedu2: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
  l_texto_titulo.place(x=490,y=90) 
  l_texto_titulo = Label(frameMeio, text=f'R$: {base_de3: ,.2F}    até       R$: {base_ate3: ,.2F}                    {inssali3:,.2f}%               R$: {dedu3: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
  l_texto_titulo.place(x=490,y=110)
  l_texto_titulo = Label(frameMeio, text=f'R$: {base_de4: ,.2F}    até       R$: {base_ate4: ,.2F}                    {inssali4:,.2f}%               R$: {dedu4: ,.2F}', font=('verdana 7'),bg=co2,fg=co1)
  l_texto_titulo.place(x=490,y=130)
  l_texto_titulo = Label(frameMeio, text=f'Teto Máximo de desconto de INSS... : R$: {teto_inss: .2f}', font=('verdana 7 bold'),bg=co3,fg=co1)
  l_texto_titulo.place(x=490,y=150)

  l_pericu = Label(frameMeio, text='  De', font=('verdana 10 bold'),bg=co2,fg=co1)
  l_pericu.place(x=50,y=50)
  l_pericu = Label(frameMeio, text='  Até ', font=('verdana 10 bold'),bg=co2,fg=co1)
  l_pericu.place(x=150,y=50)
  l_pericu = Label(frameMeio, text=' Alíquota ', font=('verdana 10 bold'),bg=co2,fg=co1)
  l_pericu.place(x=230,y=50)
  l_pericu = Label(frameMeio, text='  Dedução ', font=('verdana 10 bold'),bg=co2,fg=co1)
  l_pericu.place(x=330,y=50)
  l_pericu = Label(frameMeio, text='Teto INSS ', font=('verdana 10 bold'),bg=co2,fg=co1)
  l_pericu.place(x=30,y=150)

  #_-----------------------------------------------------------------------------


  l_salario = Label(framebaixo, text='  TABELA DE IRRF  ', font=('verdana 13 bold'),bg=co3,fg=co1)
  l_salario.place(x=600,y=0)
  l_insalu = Label(framebaixo, text=' Digite abaixo os dados para alteração da tabela ', font=('verdana 11 bold'),bg=co5,fg=co1)
  l_insalu.place(x=30,y=10)

  l_pericu = Label(framebaixo, text='  De', font=('verdana 10 bold'),bg=co3,fg=co1)
  l_pericu.place(x=50,y=50)
  l_pericu = Label(framebaixo, text='  Até ', font=('verdana 10 bold'),bg=co3,fg=co1)
  l_pericu.place(x=150,y=50)

  l_pericu = Label(framebaixo, text=' Alíquota ', font=('verdana 10 bold'),bg=co3,fg=co1)
  l_pericu.place(x=230,y=50)
  l_pericu = Label(framebaixo, text='Parc. Deduzir', font=('verdana 10 bold'),bg=co3,fg=co1)
  l_pericu.place(x=330,y=50)

  l_pericu = Label(framebaixo, text='Dedução Dependente', font=('verdana 10 bold'),bg=co3,fg=co1)
  l_pericu.place(x=30,y=180)
  l_pericu = Label(framebaixo, text='Dedução Simplificada', font=('verdana 10 bold'),bg=co3,fg=co1)
  l_pericu.place(x=30,y=200)


  l_texto_titulo = Label(framebaixo, text=f'Alíquota          Parc. Deduzir ', font=('verdana 8 bold'),bg=co5,fg=co1)
  l_texto_titulo.place(x=730,y=50)
  l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir1: ,.2F}            até       R$: {base_ateir1: ,.2F}                    {irraliir1: ,.2f}%                R$: {deduir1: ,.2F}', font=('verdana 7 '),bg=co3,fg=co1)
  l_texto_titulo.place(x=490,y=70)
  l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir2: ,.2F}    até       R$: {base_ateir2: ,.2F}                    {irraliir2:,.2f}%                 R$: {deduir2: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
  l_texto_titulo.place(x=490,y=90) 
  l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir3: ,.2F}    até       R$: {base_ateir3: ,.2F}                    {irraliir3:,.2f}%               R$: {deduir3: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
  l_texto_titulo.place(x=490,y=110)
  l_texto_titulo = Label(framebaixo, text=f'R$: {base_deir4: ,.2F}    até       R$: {base_ateir4: ,.2F}                    {irraliir4:,.2f}%               R$: {deduir4: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
  l_texto_titulo.place(x=490,y=130)
  l_texto_titulo = Label(framebaixo, text=f'         Acima  de  R$: {base_deir5: ,.2F}                                 {irraliir5:,.2f}%               R$: {deduir5: ,.2F}', font=('verdana 7'),bg=co3,fg=co1)
  l_texto_titulo.place(x=490,y=150)

  l_pericu = Label(framebaixo, text=f'Dedução Por Dependente ....   ...........: R$: {dependente: .2f}', font=('verdana 7 bold'),bg=co5,fg=co1)
  l_pericu.place(x=490,y=180)
  l_pericu = Label(framebaixo, text=f'Base de DEDUÇÃO SIMPLIFICADA...:  R$: {deducao_simplicada: .2f}', font=('verdana 7 bold'),bg=co5,fg=co1)
  l_pericu.place(x=490,y=200)
tabelas_atuais()

e_de1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_de1.place(x=30,y=70)
e_ate1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ate1.place(x=130,y=70)
e_ali1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ali1.place(x=230,y=70)
e_par1 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_par1.place(x=330,y=70)

e_de2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_de2.place(x=30,y=90)
e_ate2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ate2.place(x=130,y=90)
e_ali2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ali2.place(x=230,y=90)
e_par2 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_par2.place(x=330,y=90)

e_de3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_de3.place(x=30,y=110)
e_ate3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ate3.place(x=130,y=110)
e_ali3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ali3.place(x=230,y=110)
e_par3 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_par3.place(x=330,y=110)

e_de4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_de4.place(x=30,y=130)
e_ate4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ate4.place(x=130,y=130)
e_ali4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_ali4.place(x=230,y=130)
e_par4 = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_par4.place(x=330,y=130)

e_tetoinss = Entry(frameMeio,width=15,justify=LEFT,relief=SOLID)
e_tetoinss.place(x=130,y=150)


#--------------------------------------------------------------------


e_deir1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_deir1.place(x=30,y=70)
e_ateir1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_ateir1.place(x=130,y=70)
e_aliir1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_aliir1.place(x=230,y=70)
e_parir1 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_parir1.place(x=330,y=70)

e_deir2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_deir2.place(x=30,y=90)
e_ateir2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_ateir2.place(x=130,y=90)
e_aliir2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_aliir2.place(x=230,y=90)
e_parir2 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_parir2.place(x=330,y=90)

e_deir3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_deir3.place(x=30,y=110)
e_ateir3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_ateir3.place(x=130,y=110)
e_aliir3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_aliir3.place(x=230,y=110)
e_parir3 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_parir3.place(x=330,y=110)

e_deir4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_deir4.place(x=30,y=130)
e_ateir4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_ateir4.place(x=130,y=130)
e_aliir4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_aliir4.place(x=230,y=130)
e_parir4 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_parir4.place(x=330,y=130)

e_deir5= Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_deir5.place(x=30,y=150)
# ate5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
# ate5.place(x=130,y=150)
e_aliir5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_aliir5.place(x=230,y=150)
e_parir5 = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_parir5.place(x=330,y=150)

e_dedudep = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_dedudep.place(x=230,y=180)
e_dedusimp = Entry(framebaixo,width=15,justify=LEFT,relief=SOLID)
e_dedusimp.place(x=230,y=200)



lista1 = [      e_de1,e_ate1,e_ali1,e_par1,
                e_de2,e_ate2,e_ali2,e_par2,
                e_de3,e_ate3,e_ali3,e_par3,
               e_de4,e_ate4,e_ali4,e_par4,
                e_deir1,e_ateir1,e_aliir1,e_parir1,
                e_deir2,e_ateir2,e_aliir2,e_parir2,
                e_deir3,e_ateir3,e_aliir3,e_parir3,
                e_deir4,e_ateir4,e_aliir4,e_parir4,
                e_deir5,e_aliir5,e_parir5,e_tetoinss,
                e_dedudep,e_dedusimp ]





de1,ate1,ali1,par1,de2,ate2,ali2,par2,de3,ate3,ali3,par3,de4,ate4,ali4,par4,deir1,ateir1,aliir1,parir1,deir2,ateir2,aliir2,parir2,deir3,ateir3,aliir3,parir3,deir4,ateir4,aliir4,parir4,deir5,aliir5,parir5,tetoinss,dedudep,dedusimp = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


lista2 = [      de1,ate1,ali1,par1,
                de2,ate2,ali2,par2,
                de3,ate3,ali3,par3,
                de4,ate4,ali4,par4,
                deir1,ateir1,aliir1,parir1,
                deir2,ateir2,aliir2,parir2,
                deir3,ateir3,aliir3,parir3,
                deir4,ateir4,aliir4,parir4,
                deir5,aliir5,parir5,tetoinss,
                dedudep,dedusimp ]


# print(len(lista1))
# print(len(lista2))
# print(lista1)
# print(lista2)

def alterar():
    os.system('cls')
    cont=0
    for i in lista1:
       if i.get() == "":
           cont +=1
          
    print(cont) 
    if cont>0:
      messagebox.showerror('Erro','Preencha todos os campos')
      return
    else:
     x=0
     for i in lista1:
      dados=(i.get())
      lista2[x] = dados
      print(x,lista2[x],dados)
      x +=1
     print(lista2)
     atualizar_dados(lista2)
     tabelas_atuais()

def mostrar():
    os.system('cls')
    x=0
    y=1
    lista_itens=visualizar()
    # print(lista_itens)
    # print(len(lista_itens[0]))
    for i in range(len(lista_itens[0])):
      item=lista_itens[0][y]
      lista1[x].delete(0,'end')
      lista1[x].insert(0,item)
      x += 1
      y += 1
      if y > 38: return
      tabelas_atuais()
l_botao = Button(framebaixo,command=mostrar,width=20,text="Alterar tabelas".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 10 bold"),bg=co12,fg=co1)
l_botao.place(x=280,y=250)

l_botao = Button(framebaixo,command=alterar,width=20,text="Confirmar alteração".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 10 bold"),bg=co11,fg=co9)
l_botao.place(x=500,y=250)



janela.mainloop()