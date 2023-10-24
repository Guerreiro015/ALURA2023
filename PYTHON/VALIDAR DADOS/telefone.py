# import os
# os.system('cls')
# from validar_telefone import *
# print('ola')
# valor = '1234567444891'

# validar_tel(valor)

from validar_telefone import *
import re

telefone = "122444552126481234"
telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)