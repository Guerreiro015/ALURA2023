import os
os.system("cls")

from tkinter import *
import pandas as pd  
  
class Table: 
      
    def __init__(self,root): 
        
        for i in range(total_rows): 
            for j in range(total_columns): 
                        self.e = Entry(root, width=20, fg='black', 
                               font=('Arial',10,'bold')) 
                        self.e.grid(row=i, column=j) 
                        self.e.insert(END, dados[i][j]) 
dados = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21), 
       (5,'Shubham','Delhi',21)] 
# dados = pd.read_excel("dadas.xlsx",sheet_name="plan") 

# print()

total_rows = len(dados) 
total_columns = len(dados[0]) 
   
root = Tk() 
t = Table(root) 
root.mainloop() 


