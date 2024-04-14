# def classificar_musica(genero_favorito, genero_musica):
#     if genero_favorito == genero_musica:
#         return 'recomendada'
#     elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
#         return 'neutra'
#     else:
#         return 'não recomendada'

# resultado = classificar_musica('Rock', 'Pop')
# print(resultado)

from tkinter.filedialog import askdirectory,askopenfile
from tkinter.messagebox import askyesnocancel

# pasta = askdirectory(title='Selecione uma pasta do computador')
# print(pasta)


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


