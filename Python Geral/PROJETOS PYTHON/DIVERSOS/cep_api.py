import os
os.system('cls')
import requests
from tkinter import*
from tkinter import messagebox


codigo = str('04760060')


r = requests.get(f'https://viacep.com.br/ws/{codigo}/json/')

try:
    dados = r.json() # Mosyra o resultado em forma de dicionário
    print(dados) 
    print(dados["logradouro"])
    print(dados["bairro"])
    print(dados["localidade"])
    print(dados["uf"])
except:
    messagebox.showerror('ERRO','O Cep Digitado não é Valido')
    print('erro')

# for a in dados: # Mostrar Os campos chaves
#     print(a)

# print(dados.keys()) # Mostrar Os campos chaves 2º modo

# for i in dados: # Mostrar Os valores dos campos
#     print(dados[i])

# print(dados.values()) # Mostrar Os valores dos campos 2º modo
# print(*dados.values()) # Mostrar Os valores dos campos 2º modo

# da=dados['logradouro']
# print(da)


# for i in dados:
#     print(f'-> {i} = {dados[i]}') # Lista com todos

    
