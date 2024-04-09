# >>> arquivo = open("palavras.txt", "w")  - CRIA UM ARQUIVO, SE EXISTE O ARQUIVO CO ESTE NOME ELA SOBREPOE

# Vale lembrar que o w sobrescreve o arquivo, se o mesmo existir. Se só quisermos adicionar conteúdo ao arquivo, utilizamos o ("palavras.txt", "a")

#Agora que temos o arquivo, como escrevemos nele? Basta chamar no arquivo a função write, passando para ela o que queremos escrever no arquivo:

# >>> arquivo.write("banana")

# >>> arquivo.write("melancia")

# Quando estamos trabalhando com arquivos, devemos nos preocupar em fechá-lo. Assim como abrimos um arquivo, devemos fechá-los, chamando a função close:

# >>> arquivo.close()

# >>> arquivo = open("palavras.txt", "a")
# Podemos escrever novamente no arquivo, mas dessa vez com a preocupação de criar uma nova linha após o que vamos escrever. Para representar uma nova linha em código, adicionamos o \n ao final do que queremos escrever:

# >>> arquivo.write("morango\n")

# >>> arquivo.write("manga\n")

# arquivo = open("entrada.txt")
# Nesse caso será utilizado o modo de leitura (r) por padrão.



# Além do r, w e a existe o modificador b que devemos utilizar quando queremos trabalhar no modo binário. Para abrir uma imagem devemos usar:

# imagem = open("foto.jpg", "rb")
# Por exemplo, o código abaixo cria uma cópia de uma imagem:

# #arquivo copia.py
# logo = open('python-logo.png', 'rb')
# data = logo.read()
# logo.close()

# logo2 = open('python-logo2.png', 'wb')
# logo2.write(data)
# logo2.close()
import os
os.system("cls")

arquivo = open("palavras.txt","w") # Criar um arquivo ou substituir o conteuo de um arquivo
arquivo.write("banana\n") # adiciobar conteudo a um arquivo
arquivo.write('abacaxi\n') # adiciobar conteudo a um arquivo
arquivo.write('caju\n') # adiciobar conteudo a um arquivo
arquivo.close()
arquivo = open("palavras.txt","a") # Abrir arquivo para adiconar comteudo
arquivo.write("melancia\n") #adiciobar conteudo a um arquivo
arquivo.close()
arquivo = open("palavras.txt","r") # Abrir arquivo para ler comteudo
arquivo = open("palavras.txt") # Abrir arquivo para ler comteudo
arquivo.close()

# abaixo mnaiera de abrir e ler arquivo
with open("palavras.txt","r") as arquivo:
    ler = arquivo.read()
print(ler)

with open("email.txt","r") as arquivo_email:
    ler = arquivo_email.read()
print(ler,"\n")

with open("mensagem.txt","r") as arquivo_mensage: 
   men = arquivo_mensage.read() # .read mostra arquivo inteiro
print(men)


with open("mensagem.txt","r",encoding=("utf-8")) as arquivo_mensage: 
   men = arquivo_mensage.readlines() # .readlines mostra cada linha em formato de lista
print(men)

for linha in men:
    if "falar" in linha or "foi" in linha:
        print("\n",linha)

with open("senha.txt","w") as arquivo_senha: ### CRIANDO UM ARQUIVO
    arquivo_senha.write("12345") # write para COLOCAR um valor no arquivo senha.txt

with open("senha.txt","r") as arquivo_senha: 
   men = arquivo_senha.read() # .read mostra arquivo inteiro
print(men,"\n")

with open("senha.txt","w") as arquivo_senha: ### ALTERAR VALOR DA SENHA
    arquivo_senha.write("567890") # write para alerar vor do arquivo senha.txt

with open("senha.txt","r") as arquivo_senha: 
   men = arquivo_senha.read() # .read mostra novo arquivo senha
print(men,"\n")

with open("senha.txt","a") as arquivo_senha: ### ADICIONAR VALOR A SENHA
    arquivo_senha.write("\nTESTANDO\nSenha NOVA\nPARECE QUE\nFUNCIONOU") # write para alerar vor do arquivo senha.txt
    arquivo_senha.write("\nAbriu mesmo")
with open("senha.txt","r") as arquivo_senha: 
   men = arquivo_senha.read() # .read PARA LER O ARQUIVO de uma vez
print(men,"\n")

with open("senha.txt","r") as verificar:
    ler = verificar.readlines()
for linha in ler:
    if "QUE" in linha:
        print(linha)

for linha in ler:
    if "mesmo" in linha:
        print(linha)

os.system("cls")

with open("lista_frutas.txt","w") as arquivo:
 arquivo.write("banana\nmelancia\nmanga\nabacaxi\nmaracuja\nmorango")

import random
with open("lista_frutas.txt","r") as lista:
    ler = lista.readlines()
tamanho = len(ler)
numero = random.randrange(0,tamanho)
print(tamanho)
for linha in ler:
    if linha == ler[numero]:
        print(linha)






