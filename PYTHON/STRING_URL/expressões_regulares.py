#Expressoes regulares são uma forma de procurar um texto por padrao

import os
os.system("cls")


endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"


import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

# Vamos procurar o CEP
print(endereco,"\n")
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)

padrao = re.compile("[1234567890]{5}[-][1234567890]{3}")
busca = padrao.search(endereco)
if busca:
    print(busca.group())
else: "\n Busca não encontrada "

padrao = re.compile("[0-9]{5}[-][0-9]{3}")
busca = padrao.search(endereco)
if busca:
    print(busca.group())
else: "\n Busca não encontrada "


endereco2 = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") #Colocando ? ou {0-1}Fica opcional pode aparecer ou não
busca = padrao.search(endereco)
if busca:
    print(busca.group())

    busca = padrao.search(endereco2)
    print(busca.group())




