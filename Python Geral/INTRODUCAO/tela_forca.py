import os
os.system('cls')
def jogo():
       

    texo = ''' Testando tela
    janela de novo
    varredor'''
    resultado['text'] = texo

from tkinter import *
janela = Tk()
janela.geometry("400x400")

janela.title("BANCO DA ALURA")

cabecalho = Label(janela, text = ('clicar no botão teste'))
cabecalho2 = Label(janela, text = ('clicar AQUI'))
cabecalho.grid(column=1, row= 2, padx=30, pady=10)
cabecalho2.grid(column=1, row= 3, padx=30, pady=10)

botao = Button(janela, text = "Ver programa", command=jogo)
botao.grid(column=1, row=4, padx=30, pady=10)

resultado = Label(janela, text= (""))
resultado.grid(column= 1, row= 5, padx=30, pady=10)



janela.mainloop()
