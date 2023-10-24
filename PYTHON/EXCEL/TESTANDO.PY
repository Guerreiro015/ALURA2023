from tkinter import * 
 
from tkinter import ttk  
 
app = Tk()  
 
app.title("GUI Application of Python")  
 
ttk.Label(app, text ="Treeview(hierarchical)").pack()
 
treeview = ttk.Treeview(app)  
 
treeview.pack()  
 
treeview.insert('', '0', 'item1', 
                text ='GeeksforGeeks') 
 
treeview.insert('', '1', 'item2', 
                text ='Computer Science')
treeview.insert('', '2', 'item3', 
                text ='GATE papers')
treeview.insert('', 'end', 'item4',
                text ='Programming Languages')
 
treeview.insert('item2', 'end', 'Algorithm', 
                text ='Algorithm')  
treeview.insert('item2', 'end', 'Data structure', 
                text ='Data structure') 
treeview.insert('item3', 'end', '2018 paper', 
                text ='2018 paper')  
treeview.insert('item3', 'end', '2019 paper', 
                text ='2019 paper')
treeview.insert('item4', 'end', 'Python', 
                text ='Python')
treeview.insert('item4', 'end', 'Java', 
                text ='Java')
 
treeview.move('item2', 'item1', 'end')  
treeview.move('item3', 'item1', 'end')
treeview.move('item4', 'item1', 'end')
 
app.mainloop()