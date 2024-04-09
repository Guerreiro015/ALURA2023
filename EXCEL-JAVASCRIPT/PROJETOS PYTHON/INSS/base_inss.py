import os
os.system("cls")
from view_inss import *
lista_itens=visualizar() 

base_de1=lista_itens[0][1]
base_de2=lista_itens[0][5]
base_de3=lista_itens[0][9]
base_de4=lista_itens[0][13]
base_ate1=lista_itens[0][2]
base_ate2=lista_itens[0][6]
base_ate3=lista_itens[0][10]
base_ate4=lista_itens[0][14]
inssali1 = lista_itens[0][3]
inssali2 = lista_itens[0][7]
inssali3 = lista_itens[0][11]
inssali4 = lista_itens[0][15]
dedu1 = lista_itens[0][4]
dedu2 = lista_itens[0][8]
dedu3 = lista_itens[0][12]
dedu4 = lista_itens[0][16]

bases_inss = [base_ate1,base_ate2,base_ate3,base_ate4]
bases_inss = [1320,2571.29,3856.94,7507.49]

porcento = [inssali1,inssali2,inssali3,inssali4]
desc = [dedu1, dedu2, dedu3, dedu4]

base_deir1=lista_itens[0][17]
base_deir2=lista_itens[0][21]
base_deir3=lista_itens[0][25]
base_deir4=lista_itens[0][29]
base_deir5=lista_itens[0][33]

base_ateir1=lista_itens[0][18]
base_ateir2=lista_itens[0][22]
base_ateir3=lista_itens[0][26]
base_ateir4=lista_itens[0][30]
base_ateir5=100000000

irraliir1 = lista_itens[0][19]
irraliir2 = lista_itens[0][23]
irraliir3 = lista_itens[0][27]
irraliir4 = lista_itens[0][31]
irraliir5 = lista_itens[0][34]

deduir1 = lista_itens[0][20]
deduir2 = lista_itens[0][24]
deduir3 = lista_itens[0][28]
deduir4 = lista_itens[0][32]
deduir5 = lista_itens[0][35]

teto_inss = lista_itens[0][36]
dependente = lista_itens[0][37]
deducao_simplicada = lista_itens[0][38]

bases_irrf = [base_ateir1,base_ateir2,base_ateir3,base_ateir4,1000000]
aliq =    [irraliir1, irraliir2,   irraliir3,    irraliir4,   irraliir5  ]
desc_ir = [deduir1, deduir2, deduir3, deduir4, deduir5]



valor_inss=0
global x
x=0
def inss(valor):
    x=0
    for i in bases_inss:
        if valor > base_ate4:
          valor_inss = teto_inss
          return valor_inss
        else:
          if valor <= i:
            valor_inss = (valor*porcento[x]/100)-(desc[x])
            return valor_inss
            
          else:
            x += 1
        
def irrf(valor,x):
  x=0
  for i in bases_irrf:
      if valor <= i:
         valor_irrf = (valor*aliq[x]/100)-desc_ir[x]
         print(aliq[x])
         print(desc_ir[x])
         return valor_irrf
      else:
       x += 1
         


