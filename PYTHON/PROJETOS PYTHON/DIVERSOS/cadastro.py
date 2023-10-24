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
# imprtando os outros arquivos
from view import *


#CORES--------------------------------------------
#bg= Preenchimento
#fg= Bordas

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

# Vamos ver algumas configurações de estilo mais comuns que podemos definir:
# Width – Largura do widget;
# Height – Altura do widget;
# Text – Texto a ser exibido no widget;
# Font – Família da fonte do texto;
# Fg – Cor do texto do widget;
# Bg – Cor de fundo do widget;
# Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).


# Criando janela------------------------------

janela = Tk()
janela.title("CONTROLE DE INVENTARIO")
janela.geometry("900x800")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando  funcções

global tree
# Função inserir
def inserir():
    global imagem,imagem_string,l_immagem
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    modelo = e_marca.get()
    data = e_data.get()
    valor=e_valor.get()
    serie=e_serie.get()
    imagem=imagem_string

    lista_inserir = [nome,local,descricao,modelo,data,valor,serie,imagem]

    for i in lista_inserir:
        if i=="":
           messagebox.showerror('Erro','Preencha todos os campos')
           return
      
           

    inserir_dados(lista_inserir) 
    messagebox.showinfo('Sucesso ','Os dados foram inseridos com sucesso')

    e_nome.delete(0,"end")
    e_local.delete(0,"end")
    e_descricao.delete(0,"end")
    e_marca.delete(0,"end")
    e_data.delete(0,"end")
    e_valor.delete(0,"end")
    e_serie.delete(0,"end")
    e_nome.delete(0,"end")
       
    mostrar() 
global imagem, imagem_string, l_immagem

def verificar():
  global imagem, imagem_string, l_immagem
  try:
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
    valor = treev_lista[0]

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_data.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serie.delete(0, 'end')

    id = int(treev_lista[0])
    e_nome.insert(0, treev_lista[1])
    e_local.insert(0, treev_lista[2])
    e_descricao.insert(0, treev_lista[3])
    e_marca.insert(0, treev_lista[4])
    e_data.insert(0, treev_lista[5])
    e_valor.insert(0, treev_lista[6])
    e_serie.insert(0, treev_lista[7])
    imagem = treev_lista[8]

    imagem=Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image = imagem,bg=co1,fg=co4)
    l_imagem.place(x=700,y=0)
       
    def atualizar():
        global imagem,imagem_string, l_imagem

            
        nome = e_nome.get()
        local = e_local.get()
        descricao = e_descricao.get()
        model = e_marca.get()
        data = e_data.get()
        valor = e_valor.get()
        serie = e_serie.get()
        imagem = imagem_string

        if imagem == '':
            imagem = e_serie.insert(0, treev_lista[7])
        
        lista_atualizar = [nome, local, descricao, model, data, valor,serie,imagem, id]
        for i in lista_atualizar:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        atualizar_dados(lista_atualizar)

        messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_marca.delete(0, 'end')
        e_data.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serie.delete(0, 'end')
        b_confirmar.destroy()

        mostrar()




    b_confirmar = Button(frameMeio,command=atualizar,image=foto_update,width=95,text=" Atualizar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co5)
    b_confirmar.place(x=330,y=185)

  except IndexError:
    messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

def deletar():
   try:

    focar_dados = tree.focus()
    focar_dicionario = tree.item(focar_dados)
    focar_lista = focar_dicionario['values']
    valor = focar_lista[0]

    deletar_dados([valor])

    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_data.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serie.delete(0, 'end')
    e_nome.delete(0, 'end')

    messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

    mostrar()

   except IndexError:
    messagebox.showerror('Erro', 'Seleciona um dos dados na tabela') 

  
# Função para escolher imagens

def escolher_imagem():
        global imagem, imagem_string, l_immagem
    
        imagem = fd.askopenfilename()
        imagem_string = imagem
    #Abrindo imagem
        imagem=Image.open(imagem)
        imagem = imagem.resize((170,170))
        imagem = ImageTk.PhotoImage(imagem)

        l_imagem = Label(frameMeio, image = imagem,bg=co1,fg=co4)
        l_imagem.place(x=700,y=0)

def ver_imagem():
  try:   
     global imagem, imagem_string, l_immagem

     # Troquei treev da apostila (video) por focar
     focar_dados = tree.focus()
     focar_dicionario = tree.item(focar_dados)
     focar_lista = focar_dicionario['values']
     valor = [int(focar_lista[0])]
     item = ver_item(valor)
     imagem = item[0][8]

     imagem=Image.open(imagem)
     imagem = imagem.resize((170,170))
     imagem = ImageTk.PhotoImage(imagem)

     l_imagem = Label(frameMeio, image = imagem,bg=co1,fg=co4)
     l_imagem.place(x=700,y=0)

  except:
     messagebox.showerror('Erro', 'Não foi encontrada nenhuma imagem') 

# Criando frames-------------------------------

frameCima = Frame(janela,width=1043, height=50, bg=co1, relief=FLAT) #Tamanho do quadro
frameCima.grid(row=0,column=0) # posição do quadro

frameMeio = Frame(janela,width=1043, height=300, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW) # NSEW = Norte, Sul, lEste e Oweste

frameBaixo = Frame(janela,width=1043, height=303, bg=co1,pady=20, relief=FLAT)
frameBaixo.grid(row=2,column=0, pady=2, padx=0, sticky=NSEW)

# Preparando a imagem - FrameCima-------------------------------
foto=Image.open("inventario.png")
foto = foto.resize((45,45))
foto = ImageTk.PhotoImage(foto)

foto_logo = Label(frameCima, image = foto, text='  INVENTÁRIO DOMÉSTICO', width=900, compound=LEFT, relief=RAISED, anchor= NW, font=('verdana 20 bold'),bg=co1,fg=co4)
foto_logo.place(x=0,y=0)

# Trabahando no FrameMeio -------------------------------------

l_nome = Label(frameMeio,text="Nome", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_nome.place(x=10,y=10)
e_nome = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)# PODEMOS USAR SOLID OU ("solid")
e_nome.place(x=130,y=11)

l_local = Label(frameMeio,text="Local/Área", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_local.place(x=10,y=40)
e_local = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_local.place(x=130,y=41)

l_descricao = Label(frameMeio,text="Descrição", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_descricao.place(x=10,y=70)
e_descricao = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_descricao.place(x=130,y=71)

l_marca = Label(frameMeio,text="Marca/Modelo", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_marca.place(x=10,y=100)
e_marca = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_marca.place(x=130,y=101)

l_data = Label(frameMeio,text="Data da Compra", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_data.place(x=10,y=130)
# CRIANDO UM CALENDARIO-----------------------------------------
e_data = DateEntry(frameMeio,width=12,BackGround='darkblue',bordwidth=2,year=2023)# Criando um calendario
e_data.place(x=130,y=131)
#---------------------------------------------------------------------------------------


l_valor = Label(frameMeio,text="Valor da Compra", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_valor.place(x=10,y=160)
e_valor = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_valor.place(x=130,y=161)

l_serie = Label(frameMeio,text="Número de Serie", height=1,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co4)
l_serie.place(x=10,y=190)
e_serie = Entry(frameMeio,width=30,justify=LEFT,relief=SOLID)
e_serie.place(x=130,y=191)

#Criando botões --------------------------------------------


#Botão carregar imagem
l_img_item = Label(frameMeio,text="Imagem do ítem", compound=CENTER,anchor=NW,font=("ivy 10 bold"),bg=co1,fg=co0)
l_img_item.place(x=10,y=220)

l_img_item = Button(frameMeio,command=escolher_imagem, width=25,text="Carregar Imagem".upper(), height=1,anchor=CENTER,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_img_item.place(x=130,y=221)


#____________________________________
foto_adicionar = Image.open("Adicionar.png")
foto_adicionar = foto_adicionar.resize((20,20))
foto_adicionar = ImageTk.PhotoImage(foto_adicionar)

foto_verificar = Image.open("carregar.png")
foto_verificar = foto_verificar.resize((20,20))
foto_verificar = ImageTk.PhotoImage(foto_verificar)

foto_deletar = Image.open("lixeira.png")
foto_deletar = foto_deletar.resize((20,20))
foto_deletar = ImageTk.PhotoImage(foto_deletar)

foto_ver = Image.open("ver.png")
foto_ver = foto_ver.resize((20,20))
foto_ver = ImageTk.PhotoImage(foto_ver)

foto_update = Image.open("update.png")
foto_update = foto_update.resize((20,20))
foto_update = ImageTk.PhotoImage(foto_update)



# Botão adicionar
l_adicionar = Button(frameMeio,command=inserir,image=foto_adicionar,width=95,text="  Adicionar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_adicionar.place(x=330,y=10)

# Botão verificar
l_verificar = Button(frameMeio,command=verificar,image=foto_verificar,width=95,text="  Verificar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_verificar.place(x=330,y=50)

# Botão Deletar
l_deletar = Button(frameMeio,command=deletar,image=foto_deletar,width=95,text="  Deletar".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_deletar.place(x=330,y=90)

# Botão Mostrar
l_ver_item = Button(frameMeio,command=ver_imagem,image=foto_ver,width=95,text="  Ver Ítens".upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=("ivy 8 bold"),bg=co1,fg=co4)
l_ver_item.place(x=330,y=220)


# Frames dos totais
l_total = Label(frameMeio,text="         Valor Total dos Ítens           ",height=2,anchor=NW,font=("ivy 10 bold"),bg=co9,fg=co8)
l_total.place(x=460,y=10)
l_total = Label(frameMeio,text="",width=15, height=2,anchor=CENTER,font=("ivy 17 bold"),bg=co7,fg=co1)
l_total.place(x=460,y=30)


l_quant = Label(frameMeio,text="      Quantidade Total dos Ítens    ", height=2,anchor=NW,font=("ivy 10 bold"),bg=co9,fg=co8)
l_quant.place(x=460,y=110)
l_quant = Label(frameMeio,text="",width=15, height=2,anchor=CENTER,font=("ivy 17 bold"),bg=co7,fg=co1)
l_quant.place(x=460,y=130)

#-----------------------------------------------------------
# tabela -TABELA ------TABELA   TABELA----------------------------------------------------------

# Criando cabeçalho da tabela  duas barras de rolagem with dual scrollbars
def mostrar():
    global tree
    tabela_head = [' Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = visualizar()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
    # ( tree é o nome da tabela) --------------------------
    # vertical scrollbar -- Barra de rolagem
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar -- Barra de rolagem
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajusta a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = f'R$ {Total_valor:,.2f}'
    l_quant['text'] = Total_itens
#_______________________________________________________________
    # imagem = lista_itens[0][8]

    # imagem=Image.open(imagem)
    # imagem = imagem.resize((170,170))
    # imagem = ImageTk.PhotoImage(imagem)

    # l_imagem = Label(frameMeio, image = imagem,bg=co1,fg=co4)
    # l_imagem.place(x=700,y=0)
     
#______________________________________________________________________
mostrar()



janela.mainloop()

