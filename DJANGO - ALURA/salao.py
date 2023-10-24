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

frame1 = tkinter.LabelFrame(frame, text = 'Informações do Cliente',font=' ivy 10 bold')
frame1.grid(row=0,column=0,padx=10,pady=5)


nome_label = tkinter.Label(frame1,text='Nome do Cliente')
nome_label.grid(row=0,column=0,pady=0)
nome_entry = tkinter.Entry(frame1,width=25)
nome_entry.grid(row=1,column=0,)

cpf_label = tkinter.Label(frame1,text='CPF: ')
cpf_label.grid(row=0,column=1)
cpf_entry = tkinter.Entry(frame1)
cpf_entry.grid(row=1,column=1)

tel_label = tkinter.Label(frame1,text='Telefone')
tel_label.grid(row=0,column=2)
tel_entry = tkinter.Entry(frame1)
tel_entry.grid(row=1,column=2)

email_label=tkinter.Label(frame1,text='Email')
email_label.grid(row=0,column=3)
email_entry=tkinter.Entry(frame1,width=25)
email_entry.grid(row=1,column=3)

cad_label=tkinter.Label(frame1,text='Data do Cadastro')
cad_label.grid(row=0,column=4)
cad_entry=DateEntry(frame1)
cad_entry.grid(row=1,column=4)


cep_label=tkinter.Label(frame1,text='Número do CEP:')
cep_label.grid(row=0,column=4)
cep_entry=tkinter.Entry(frame1,bg='#F0F8FF')
cep_entry.grid(row=1,column=4)



rua_label = tkinter.Label(frame1,text='Rua:')
rua_label.grid(row=3,column=0)
rua_entry = tkinter.Entry(frame1,width=28)
rua_entry.grid(row=4, column=0)


numero_label = tkinter.Label(frame1,text='Número:')
numero_label.grid(row=3,column=1)
numero_entry = tkinter.Entry(frame1,width=10)
numero_entry.grid(row=4, column=1)

bairro_label = tkinter.Label(frame1,text='Bairro:')
bairro_label.grid(row=3,column=2)
bairro_entry = tkinter.Entry(frame1)
bairro_entry.grid(row=4, column=2)

cidade_label = tkinter.Label(frame1,text='Cidade:')
cidade_label.grid(row=3,column=3)
cidade_entry = tkinter.Entry(frame1)
cidade_entry.grid(row=4, column=3)

estado_label = tkinter.Label(frame1,text='Estado:')
estado_label.grid(row=3,column=4)
estado_entry = tkinter.Entry(frame1,border=5,justify=CENTER)
estado_entry.grid(row=4, column=4)

ddd_label = tkinter.Label(frame1,text='DDD:')
ddd_label.grid(row=3,column=5)
ddd_entry = tkinter.Entry(frame1,width=10,border=5,justify=CENTER) # Justify(center,left,right)
ddd_entry.grid(row=4, column=5)



def cep():
        
    try:
        codigo=str(cep_entry.get())
        
        r = requests.get(f'https://viacep.com.br/ws/{codigo}/json/')
        dados = r.json() 

        endereco=[rua_entry,bairro_entry,cidade_entry,estado_entry,ddd_entry,cep_entry]
        for i in endereco:
            i.delete(0,'end')
        
        rua_entry.insert(0,dados["logradouro"])
        bairro_entry.insert(0,dados["bairro"])
        cidade_entry.insert(0,dados["localidade"])
        estado_entry.insert(0,dados["uf"])
        ddd_entry.insert(0,dados["ddd"])
        ce1=codigo[:5]
        ce2=codigo[5:]
        cep_entry.insert(0, (ce1,'-',ce2))
        
            
    except:
        messagebox.showerror('CEP NÃO EXISTE','O Cep Digitado não é Valido')
        

xxx4=tkinter.Button(frame1,text='Consultar CEP:',bg='#F0F8FF',command=cep,border=4)
xxx4.grid(row=0,column=5)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)

    #-------------------------------------------------------------------

frame2 = tkinter.LabelFrame(frame,text='Dados do Serviço',font=' ivy 10 bold')
frame2.grid(row=2,column=0,padx=10,pady=5)

servico_label = tkinter.Label(frame2,text='Servico Executado')
servico_label.grid(row=0,column=0)
servico_entry=tkinter.Entry(frame2,width=30)
servico_entry.grid(row=1,column=0)

data_servico_label = tkinter.Label(frame2,text='Data do Servico')
data_servico_label.grid(row=0,column=1)
data_servico_entry = DateEntry(frame2)
data_servico_entry.grid(row=1,column=1)

atendente_label = tkinter.Label(frame2,text='Atendente: ')
atendente_label.grid(row=0,column=2)
atendente_entry = tkinter.Entry(frame2,width=23)
atendente_entry.grid(row=1,column=2)

comissao_percentual_label = tkinter.Label(frame2,text='% Comissão: ')
comissao_percentual_label.grid(row=0,column=3)
comissao_percentual_entry = tkinter.Entry(frame2)
comissao_percentual_entry.grid(row=1,column=3)

comissao_label=tkinter.Label(frame2,text='Valor Comissão:')
comissao_label.grid(row=0,column=4)
comissao_entry=tkinter.Entry(frame2)
comissao_entry.grid(row=1,column=4)

valor_label = tkinter.Label(frame2,text='Valor do Servico')
valor_label.grid(row=2,column=0)
valor_entry = tkinter.Entry(frame2)
valor_entry.grid(row=3,column=0)

parcela_label=tkinter.Label(frame2,text='Quant. Parcelas')
parcela_label.grid(row=2,column=1)
parcelas_spinbox=tkinter.Spinbox(frame2,from_=1,to='infinity',width=5)
parcelas_spinbox.grid(row=3,column=1)


def valor_parcela():
 try:
    if valor_entry.get()=='':
        va=0
        
    else:
        va=float(valor_entry.get())
        

    if comissao_percentual_entry.get() == '':
        por=0
    else:
        por=float(comissao_percentual_entry.get())

    prestacao=va/int(parcelas_spinbox.get())
    valor_parcela_entry.delete(0,'end')
    valor_parcela_entry.insert(0,f'R$:  {prestacao:,.2f}')
   
    comissao=va*por/100
    comissao_entry.delete(0,'end')
    comissao_entry.insert(0,f'R$:  {comissao:,.2f}')

    
 except:  
     messagebox.showerror(' É sério? você digitou letra ?', 'Os valores tem que ser números')

valor_parcela_label=tkinter.Button(frame2,text='Valor das parcela',command=valor_parcela,border=4,)
valor_parcela_label.grid(row=2,column=2)
valor_parcela_entry=tkinter.Entry(frame2)
valor_parcela_entry.grid(row=3,column=2)

entrada_label=tkinter.Label(frame2,text='ENTRADA')
entrada_label.grid(row=2,column=3)
var_entrada=tkinter.StringVar(value='Sem entrada')
entrada_entry=tkinter.Checkbutton(frame2,text='Com entrada',variable=var_entrada,onvalue='Com Entrada',offvalue='Sem Entrada')
entrada_entry.grid(row=3,column=3)

forma_pag_label=tkinter.Label(frame2,text='Forma de Pagamento')
forma_pag_label.grid(row=2,column=4)
forma_pag_entry=ttk.Combobox(frame2,values=['Pix','Dinheiro','Débito','Crédito','Fiado','Cortesia da casa'])
forma_pag_entry.grid(row=3,column=4)

def dados_tabela():
     conn = sqlite3.connect('salao.db')
     treev_dados = tree.focus()
     treev_dicionario = tree.item(treev_dados)
     treev_lista = treev_dicionario['values']
     no=nome_entry.get()
     cp=cpf_entry.get()
     te=tel_entry.get()
     em=email_entry.get()
     ca=cad_entry.get()
     ce=cep_entry.get()
     ru=rua_entry.get()
     nu=numero_entry.get()
     ba=bairro_entry.get()
     ci=cidade_entry.get()
     uf=estado_entry.get()
     dd=ddd_entry.get()
     se=servico_entry.get()
     da=data_servico_entry.get()
     va=valor_entry.get()
     pa=parcelas_spinbox.get()
     vp=valor_parcela_entry.get()
     co=comissao_percentual_entry.get()
     cco=comissao_entry.get()
     fo=forma_pag_entry.get()  
     id=treev_lista[0]

     lista_dados = (no,cp,te,em,ca,ce,ru,nu,ba,ci,uf,dd,se,da,va,pa,vp,co,cco,fo,id) 
     return lista_dados


def cadastro():
 try:
     no=nome_entry.get()
     cp=cpf_entry.get()
     te=tel_entry.get()
     em=email_entry.get()
     ca=cad_entry.get()
     ce=cep_entry.get()
     ru=rua_entry.get()
     nu=numero_entry.get()
     ba=bairro_entry.get()
     ci=cidade_entry.get()
     uf=estado_entry.get()
     dd=ddd_entry.get()
     se=servico_entry.get()
     da=data_servico_entry.get()
     va=valor_entry.get()
     pa=parcelas_spinbox.get()
     vp=valor_parcela_entry.get()
     co=comissao_percentual_entry.get()
     cco=comissao_entry.get()
     fo=forma_pag_entry.get()  

     lista = (no,cp,te,em,ca,ce,ru,nu,ba,ci,uf,dd,se,da,va,pa,vp,co,cco,fo) 

     if len(cp) != 11:
         messagebox.showerror('ERRO NO CPF','Verifique -  o CPF digitado é Ínválido]') 
     else:  
        cpp=f'{cp[:3]}.{cp[3:6]}.{cp[6:9]}-{cp[9:11]}'
        cpf_entry.delete(0,'end')
        cpf_entry.insert(0,cpp)
        cp=cpp
        x=0
        for i in lista:
          if i == "":
                x += 1

        if x > 0:
                messagebox.showerror('Errro','Preencha todos os dados e tente novamente') 
        else:  
                # Create Table
                conn = sqlite3.connect('salao.db')
                table_create_query = '''CREATE TABLE IF NOT EXISTS salao_base 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, nome, TEXT, cpf TEXT, tel TEXT, email TEXT, cadastro TEXT, cep TEXT, 
                rua TEXT, numero TEXT, bairro TEXT, cidade TEXT, uf TEXT, ddd TEXT, servico TEXT, d_servico TEXT,
                valor FLOAT,q_parcela FLOAT, parcela FLOAT, com FLOAT, comissao FLOAT, forma TEXT)'''
                        
                conn.execute(table_create_query)
                        
                # Insert Data
                insert_query = '''INSERT INTO salao_base 
                                (nome , cpf , tel , email , cadastro , cep,
                                rua , numero, bairro ,cidade ,uf ,ddd ,servico ,d_servico ,
                                valor ,q_parcela , parcela ,com , comissao, forma ) VALUES 
                                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )'''
                
                
                x=int(pa)
                y = int(pa)
                a=da
                dias=30
                
                for i in range(0,x):
                    pa=float(pa)
                    pa=(pa-x)+1
                    insert_tuple = (no,cp,te,em,ca,ce,ru,nu,ba,ci,uf,dd,se,da,va,pa,vp,co,cco,fo)
                    cursor = conn.cursor()

                    cursor.execute(insert_query, insert_tuple)
                    conn.commit()

                    
                    if x>1:
                        x=x-1

                        pa=float(y)

                        valor1=datetime.strptime(da,'%d/%m/%Y').date()
                        val=timedelta(dias)
                        valor2=(valor1+val)
                        da=datetime.strftime(valor2,'%d/%m/%Y')
                    
                conn.close()    
                
                messagebox.showinfo('Sucesso ','Os dados foram inseridos com sucesso')
                mostrar()
 except:       
    messagebox.showerror('Errro','Verifique os dados e tente novamente')
          

def limpar():
     nome_entry.delete(0,'end')
     cpf_entry.delete(0,'end')
     tel_entry.delete(0,'end')
     email_entry.delete(0,'end')
     cad_entry.delete(0,'end')
     cep_entry.delete(0,'end')
     rua_entry.delete(0,'end')
     numero_entry.delete(0,'end')
     bairro_entry.delete(0,'end')
     cidade_entry.delete(0,'end')
     estado_entry.delete(0,'end')
     ddd_entry.delete(0,'end')
     servico_entry.delete(0,'end')
     data_servico_entry.delete(0,'end')
     valor_entry.delete(0,'end')
     parcelas_spinbox.delete(0,'end')
     valor_parcela_entry.delete(0,'end')
     comissao_percentual_entry.delete(0,'end')
     comissao_entry.delete(0,'end')
     forma_pag_entry.delete(0,'end')


for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=3)

#---------------------------------------------------------

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

frame3 = tkinter.LabelFrame(frame,bg='bisque',fg='green',font='ivy 8 ')
frame3.grid(row=3,column=0,padx=10,pady=5)

def mostrar():
    global tree
    visualizar()
    tabela_head = ['INDICE','NOME','CPF','TELEFONE','E-MAIL','CADASTRO','CEP','RUA','NÚMERO','BAIRRO','CIDADE','UF',
                   'DDD','SERVIÇO','DATA SERVIÇO', 'Vlr. SERVICO','Quant. PARCELAS','Vlr. PARCELAS','% COMISSÃO','Vlr. COMISSÃO','FORMA DE PG']
    
    tree = ttk.Treeview(frame3, selectmode='extended',columns=tabela_head, show="headings",height=10)
    # ( tree é o nome da tabela) --------------------------

    # ajusta a largura da coluna para a string do cabeçalho
    for i in tabela_head:
        tree.column(i,anchor='center', width=43)
        tree.heading(i, text= i)

    # vertical scrollbar -- Barra de rolagem
    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)

    # horizontal scrollbar -- Barra de rolagem
    hsb = ttk.Scrollbar(frame3, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(row=0,column=1, sticky='ns')
    hsb.grid(row=1,column=0, sticky='ew')
    frame3.grid_rowconfigure(0, weight=5)
    frame3.grid_columnconfigure(0, weight=5)
    
    
    
    lista_itens = visualizar()
   # inserindo os itens dentro da tabela
        
    for item in lista_itens:
    
        tree.insert('', 'end', values=item)

mostrar()

def verificar():
   try: 
    global tree
   
    base=[nome_entry, cpf_entry, tel_entry, email_entry, cad_entry, cep_entry, rua_entry, numero_entry, bairro_entry, cidade_entry,
          estado_entry, ddd_entry,servico_entry, data_servico_entry, valor_entry, parcelas_spinbox, valor_parcela_entry,
            comissao_percentual_entry, comissao_entry, forma_pag_entry]

    for i in base:
        i.delete(0,'end')  

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
   
    x=1
    for i in base:
        i.insert(0,treev_lista[x])
        x +=1
   except:
       messagebox.showerror('ERRO','Nenhum dado selecionado')


def atualizar_dados():
   try:  
     lista=dados_tabela()
    
     with conn:
        cur = conn.cursor()
        query = '''UPDATE salao_base SET nome=?, cpf=?, tel=?, email=?, cadastro=?,
        cep=?,rua=?, numero=?, bairro=?,cidade=?,uf=?,ddd=?,servico=?,d_servico=?,
        valor=?,q_parcela=?, parcela=?,com=?, comissao=?, forma=? WHERE id=?'''
        cur.execute(query,lista)
        messagebox.showinfo('SUCESSO', 'Os dados foram alterados com sucesso')
     mostrar()

   except:
       messagebox.showerror('ERRRO!!!','Selecione um registro para alteração')


def deletar_dados():

  try:  
    
    lista=dados_tabela()    
    i=int(lista[20])
    i=[i]
    
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM salao_base WHERE id=?"
        cur.execute(query,i)      


    limpar()   
    mostrar()
    messagebox.showinfo('SUCESSO', 'Os dados foram deletados com sucesso')

  except:
    messagebox.showerror('ERRRO!!!','Selecione um registro apagar')


botao_verificar=tkinter.Button(frame2,text='Ver  Dados'.upper(),anchor='center',font='ivy 8 bold',bg='blue',fg=co1,border=4,command=verificar,width=25)
botao_verificar.grid(row=4,column=0)

limpar_botao=tkinter.Button(frame2,command=limpar,text='Limpar Dados'.upper(),anchor='center',font='ivy 8 bold',fg='Blue',border=4,width=22)
limpar_botao.grid(row=4,column=1,pady=10)

botao_verificar=tkinter.Button(frame2,text='ALTERAR DADOS'.upper(),font='ivy 8 bold',bg=co12,fg=co1,border=4,command=atualizar_dados,width=25)
botao_verificar.grid(row=4,column=2)


salvar_botao=tkinter.Button(frame2,command=cadastro,text='Salvar Dados'.upper(),anchor='center',font='Ivy 8 bold',bg='BLUE',fg=co9,width=25,border=4)
salvar_botao.grid(row=4,column=4,pady=10)

salvar_botao=tkinter.Button(frame2,command=deletar_dados,text='Apagar Dados'.upper(),anchor='center',font='Ivy 8 bold',bg=co11,fg=co9,width=22,border=4)
salvar_botao.grid(row=4,column=3,pady=10)


janela.mainloop()



