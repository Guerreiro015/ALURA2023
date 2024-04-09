# A maneira correta de abrir um arquivo
# Desta maneira o arquivo é aberto e fechado automaticamente e evita travamentos 


with open("modo.txt","w") as moelo: # Abrir para escreverr
    moelo.write("\nhoje vai ter pagamento\n")

with open("modo.txt",'r') as moelo: # Abrir para ler
    mo = moelo.read()
print(mo)

from base_inss import *

inss(500)

a= inss(500)
print(a)