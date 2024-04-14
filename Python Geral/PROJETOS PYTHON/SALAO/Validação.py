
from tkinter.filedialog import askdirectory,askopenfile
from tkinter.messagebox import askyesnocancel


confirma=""
while confirma != None:
    confirma = askyesnocancel(title='Confirmação',message='Voce Realmemte quer iniciar')
    print(confirma)
    if confirma==True:
        print('Verdade')
    elif confirma==False:
        print('Mentira')
    else:
        print('Cancela')


