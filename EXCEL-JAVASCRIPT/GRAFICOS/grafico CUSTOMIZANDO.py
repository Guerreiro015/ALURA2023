import os
os.system('cls')

import pandas as pd
# IPython_default = plt.rcParams.copy()
# plt.style.use('fivethirtyeight')

df = pd.read_csv('imigrantes.csv')
print(df)


df.set_index('País',inplace=True) # Colocar o culuna pais como indice
print(df)


anos=list(map(str,range(1980,2014))) # Crianndo uma lista com os anos como strings
print(anos)

#Extração da série de dados para o Brasil
#criamos uma variável chamada brasil igual à df.loc[]
# e variável anos nos colchetes.

brasil=df.loc['Colômbia',anos]

print(brasil)

#Vamos criar um dataframe com as informaçoes da variavel brasil

#primeito vamos criar um dicionario com os dados

brasil_dicio={'ano': brasil.index.tolist(),'imigrantes': brasil.values.tolist()} # tolist para criar a lista

print(brasil_dicio)

dados_brasil=pd.DataFrame(brasil_dicio)

print(dados_brasil)

# VAMOS USAR O PARAMETRO FIG, AX

import matplotlib.pyplot as plt


fig,ax = plt.subplots(figsize=(10,5))

ax.plot(dados_brasil['ano'],dados_brasil['imigrantes'],lw=3,marker='o',color='g') 
# (lw=espessura do gráfico) 
# - marker= marcador no gráfico pode ser qualqyer letra
# color='g' para ccolorir a linha do gráfico

ax.set_title('Imigração da Colômbia para o canadá \n Entres os anos de 1980 a 2013',fontsize=18,loc='left') 
ax.set_xlabel('Anos',fontsize=18)# Rótulos da gráfico horizontal
ax.set_ylabel('Quant. de Imigrantes',fontsize=14)# Rótulos do gráfico vertical
ax.xaxis.set_tick_params(labelsize=12) # Alterar fonte dos eixos x
ax.yaxis.set_tick_params(labelsize=12,color='red') # Alterar fonte dos eixos y

ax.xaxis.set_major_locator(plt.MultipleLocator(5))## vamos mostrar de 5 em 5 anos para nãoficar muito amontoado
ax.grid(linestyle='--') # grade no gráfico

plt.show()





