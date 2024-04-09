class data():
    import os
    os.system("cls")
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
   
    def data_formadada(self):
      print (self.dia,"/",self.mes,"/",self.ano)
     

d=data(21,11,2007)
d.data_formadada()


from datetime import date

data = date.today()
print(data)

datas = f"{data.day}/{data.month}/{data.year}"
print(datas)

data_certa = data.strftime('%d/%m/%Y') # y maiúsculo para imprimir ano com 4 digitos
print(data_certa)

from datetime import datetime

data_hora = datetime.now()

horas = data_hora.strftime('%d/%m/%Y')
print(horas)

horas = data_hora.strftime('%d/%m/%Y %H:%M:%S')
print(horas)






