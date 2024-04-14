import os
os.system("cls")

import time

class time:
  def __init__(self,horas,minutos,segundos = None):
      self._horas = horas
      self._minutos = minutos
      self._segundos = segundos

  def __str__(self):
       return '%.2d:%.2d:%.2d' % (self._horas, self._minutos, self._segundos)
       
hora = time(9,45,3)

print (hora)









# import time

# # parte do seu código

# tempo_inicial(time.time()) # em segundos

# #parte do código que vamos verificar o tempo de execução

# tempo_final(time.time()) # em segundos

# #Restante do código

# #Print do tempo que demorou para rodar a parte específica do código
# print(f"{tempo_final - tempo_inicial} segundos)