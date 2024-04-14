import os
os.system("cls")
#VAMOS TRABALHAR COM FATIAMENTO


url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
moeda = 'bytebank.com/cambio?moedaOrigem=real'


def imprime(a=None,b=None,c=None):
    print(a,f" --- Executando {c}")
    print(b,f" --- Executando {c}\n")


###########################################################
# 2ª parte - se der erro 

url = ""
len(url)

print(len(url))

#Como a variavel esta vazia não retorna nada então vamos mostrar o erro

if url == "u":
    raise ValueError("O valor esta vazio")
else:
    print(url)



url = "    a      "
print(len(url))

# se a url estiver com expaços vazios precisamos fazer uma limpeza

url=url.replace(" ","")#  vai trocaf os espaços em branco por nada
print(len(url))
print(url)






