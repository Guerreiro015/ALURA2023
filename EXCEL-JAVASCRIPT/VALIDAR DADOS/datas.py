import os
os.system('cls')

from datetime import datetime,timedelta
from validar_datas import data_br

cad = data_br()
print(cad.momento)
print(cad.mes_cadastro())
print(cad.dia_cadastro())
print(cad.data_formatada())

print(cad)

print(datetime.today())

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1)
amanha1 = datetime.today() + timedelta(days=1, hours= 20)
amanha2 = datetime.today() + timedelta(hours = 20)

resu = amanha - hoje
resu1 = amanha1 - hoje
resu2 = amanha - hoje

print(resu)
print(resu1)
print(resu2)

print(cad.tempo())



