import os
os.system("cls")

# Exemplos de URLs válidas:

# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio
# Exemplos de URLs inválidas:

# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio

import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
padrao_url2 = re.compile("(http(s)?(www.)?meubanco.com(.br)?/cambio)")
busca = padrao_url.match(url)

if not busca:
    print( " Não é uma url valida")
    #raise ValueError("A URL não é válida.") #Fazer o programa travar neste erro
else:
    print("A URL é válida")