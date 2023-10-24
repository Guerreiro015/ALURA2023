import os
os.system('cls')
import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar, DateEntry

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Aceito":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            parce = parcelas_spinbox.get()
            parcela = valor_parcela_entry.get()

            print("Nome: ", firstname, "Sobrenome: ", lastname)
            print("Título: ", title, "Idade: ", age, "Nacionalidade: ", nationality)
            print("Cursos: ", numcourses, "Semestre: ", numsemesters)
            print("Status do Registro: ", registration_status)
            print("------------------------------------------")
            
            # Create Table
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                    registration_status TEXT, num_courses INT, num_semesters INT,parcela FLOAT)
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
            age, nationality, registration_status, num_courses, num_semesters,parcela) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            insert_tuple = (firstname, lastname, title, age, nationality, registration_status, numcourses, numsemesters,parcela)
            cursor = conn.cursor()

            x=int(parce)
            for i in range(0,x):
                cursor.execute(insert_query, insert_tuple)
                conn.commit()
            conn.close()    

            # firstname.delete(0,'end')
            # lastname.delete(0,'end')
            # title.delete(0,'end')
            # age.delete(0,'end')
            # nationality.delete(0,'end')
            # numcourses.delete(0,'end')
            # numsemesters.delete(0,'end')
            # registration_status.delete(0,'end')
 


            tkinter.messagebox.showwarning(title="SUCESSO", message="Aluno cadatrado com sucesso!!.")
            
                
        else:
            tkinter.messagebox.showwarning(title="Error", message="Precisa preencher os campos nome e sobrenomes.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="Você não aceitou os termos e condições")

janela = tkinter.Tk()
janela.title("TESTE de FORMULÁRIO")

frame = tkinter.Frame(janela)
frame.pack()

# Saving User Info
frame1 =tkinter.LabelFrame(frame, text="Informação Usuário")
frame1.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(frame1, text="Primeiro Nome")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(frame1, text="Último Nome")
last_name_label.grid(row=0, column=1)


first_name_entry = tkinter.Entry(frame1)
last_name_entry = tkinter.Entry(frame1)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(frame1, text="Título")
title_combobox = ttk.Combobox(frame1, values=["", "Mr.", "Ms.", "Dr.",'Dra. ','Sr. ','Sra'])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(frame1, text="Idade")
age_spinbox = tkinter.Spinbox(frame1, from_=0, to=200)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(frame1, text="Nacionalidade")
nationality_combobox = ttk.Combobox(frame1, values=["Africa", "America do Norte", "Oceania", "America do Sul", "Antarctica", "Asia", 'Brasil', "Europa",])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

inicio_label = tkinter.Label(frame1, text="Inicio do Curso")
inicio_label.grid(row=2, column=2)
inicio_entry = DateEntry(frame1)
inicio_entry.grid(row=3, column=2)


for widget in frame1.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
frame2 = tkinter.LabelFrame(frame,text="CURSOS")
frame2.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(frame2, text="Status do Registro")

reg_status_var = tkinter.StringVar(value="Não Registrado")
registered_check = tkinter.Checkbutton(frame2, text="Registrado",
                                       variable=reg_status_var, onvalue="Registrado", offvalue="Não Registrado")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(frame2, text= "Cursos Finalizados")
numcourses_spinbox = tkinter.Spinbox(frame2, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(frame2, text="Semestre")
numsemesters_spinbox = tkinter.Spinbox(frame2, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=15, pady=5)

# Pagamento
frame3 = tkinter.LabelFrame(frame, text="Dados do Pagamento")
frame3.grid(row=2, column=0, sticky="news", padx=20, pady=15)

valor_label = tkinter.Label(frame3,text='Valor do Curso')
valor_label.grid(row=0,column=0)
parcelas_label=tkinter.Label(frame3,text='Quant. Parcelas')
parcelas_label.grid(row=0,column=1)
valor_parcela_entry=tkinter.Entry(frame3)
valor_parcela_entry.grid(row=1,column=2)


valor_entry = tkinter.Entry(frame3)
valor_entry.grid(row=1,column=0)
parcelas_spinbox=tkinter.Spinbox(frame3,from_=1, to='infinity')
parcelas_spinbox.grid(row=1,column=1)

def valor_parcela():

    if valor_entry.get()=='':
        va=0
    else:
        va=float(valor_entry.get())
    prestacao=va/float(parcelas_spinbox.get())
    valor_parcela_entry.delete(0, 'end')
    valor_parcela_entry.insert(0, f'R$: {prestacao:,.2f}')
        

button_parcela = tkinter.Button(frame3,text='Valor das Parcelas',command=valor_parcela,bg="#e9edf5")
button_parcela.grid(row=0,column=2)

for widget in frame3.winfo_children():
    widget.grid_configure(padx=15, pady=10)

# Accept terms
frame4 = tkinter.LabelFrame(frame,text='Terms & Conditions')
frame4.grid(row=3,column=0,sticky='news',padx=20,pady=10)

accept_var = tkinter.StringVar(value="Não Aceito")
terms_check = tkinter.Checkbutton(frame4, text= "Eu aceito os termos e condições.",
                                  variable=accept_var, onvalue="Aceito", offvalue="Não Aceito")
terms_check.grid(row=0, column=0)

for widget in frame4.winfo_children():
    widget.grid_configure(padx=15, pady=5)


# Button
button = tkinter.Button(frame, text="Confirmar Cadastro", command = enter_data,bg="#e9edf5")
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
 
janela.mainloop()