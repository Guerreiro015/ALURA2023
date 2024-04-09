import os
os.system('cls')

import re

padrao = '[0-9][a-z][0-9]' # Este padrao siginifica uma numero, uma letra e um numero
padrao1 = '[0-9][a-z]{2}[0-9]' # Este padrao siginifica uma numero, duas letra e um numero

texto = '123, a12 1a3 1bb2 3df4 asd '


busca = re.search(padrao,texto) # Vai buscar o padrao dentro do texto
busca1 = re.search(padrao1,texto) # Vai buscar o padrao dentro do texto
busca1 = re.search(padrao1,texto) # Vai buscar o padrao dentro do texto

print(busca) # Mostra a primeira condição sastifazida com a localização
print(busca.group())# Mostra a primeira condição sastifazida
print(busca1.group())# Mostra a primeira condição sastifazida

#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

padrao2 = '\w{1,50}@\w{1,10}.\w{1,5}.\w{1,3}'
padrao3 = '\w{1,50}@\w{1,10}.com.br'

texto2 = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"

busca2 = re.search(padrao2,texto2) # Vai buscar o padrao dentro do texto
busca3 = re.search(padrao3,texto2) # Vai buscar o padrao dentro do texto

print(busca2.group())# Mostra a primeira condição sastifazida
print(busca3.group())# Mostra a primeira condição sastifazida
