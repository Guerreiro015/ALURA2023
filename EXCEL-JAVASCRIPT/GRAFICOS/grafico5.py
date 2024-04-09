import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imigrantes.csv')
print(df)


df.set_index('País',inplace=True) # Colocar o culuna pais como indice
print(df)


anos=list(map(str,range(1980,2014))) # Crianndo uma lista com os anos como strings
print(anos)

#Extração da série de dados para o Brasil
#criamos uma variável chamada brasil igual à df.loc[]
# e variável anos nos colchetes.

brasil=df.loc[['Brasil','Peru','Cuba','Argentina'],anos]

print(brasil)

#Vamos criar um dataframe com as informaçoes da variavel brasil

#primeito vamos criar um dicionario com os dados

paises=brasil.T

print(paises)

import matplotlib.pyplot as plt

fig,axs = plt.subplots(2,2,figsize=(12,5)) # Colocamos 1, 2 para dizermos qye serao dois gráficos
fig.subplots_adjust(hspace=0.7,wspace=0.3)
fig.suptitle('IMIGRAÇÃO PARA O CANADÁ DOS 4 PAISES DA AMÉRICA DO SUL Entres os anos de 1980 a 2013')

axs[0,0].plot(paises['Brasil'],label='Brasil')
axs[0,0].set_title('Imigração do Brasil para o canadá')

axs[0,1].plot(paises['Argentina'],label='Argentina')
axs[0,1].set_title('Imigração da Argentina para o canadá ')


axs[1,0].plot(paises['Cuba'],label='Cuba')
axs[1,0].set_title('Imigração da Colombia para o canadá')

axs[1,1].plot(paises['Peru'],label='Peru')
axs[1,1].set_title('Imigração da Peru para o canadá ')


for ax in axs.flat:
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))## vamos mostrar de 5 em 5 anos para nãoficar muito amontoado todos ao mesmo tempo

for ax in axs.flat:
    ax.set_xlabel('Anos')# Rótulos da gráfico horizontal todos ao mesmo tempo
    ax.set_ylabel('Quant. de Imigrantes')# Rótulos do gráfico vertical todos ao mesmo tempo
    ax.grid() #todos ao mesmo tempo
ymin = 0
ymax = 3000

for ax in axs.ravel():
  ax.set_ylim(ymin, ymax)

# Vamos aplicar o mesmo numero do eixo y vertical para todos
ymin=0
ymax=3000

for ax in axs.ravel():
   ax.set_ylim(ymin,ymax)


plt.show()





