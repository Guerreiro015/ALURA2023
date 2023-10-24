import os
os.system('cls')
from validar_cep import cep
import requests

codigo = 12312340
codigo1 = 123123409999900
codigo2 = str('04760060')

print(cep(codigo))
#print(cep(codigo1))
print(cep(codigo2))
# cep(codigo)
# cep(codigo2)

r = requests.get('https://viacep.com.br/ws/05857390/json/')
print(r.text) # mostra o resultado em forma de texto
dados = r.json() # Mosyra o resultado em forma de dicionário

#VAMOS TRABALHAR COM O DICIONÁRIO

print(dados)
print(dados["bairro"])


for a in dados: # Mostrar Os campos chaves
    print(a)

print(dados.keys()) # Mostrar Os campos chaves 2º modo

for i in dados: # Mostrar Os valores dos campos
    print(dados[i])

print(dados.values()) # Mostrar Os valores dos campos 2º modo
print(*dados.values()) # Mostrar Os valores dos campos 2º modo

for i in dados:
    print(f'-> {i} = {dados[i]}') # Lista com todos

    
