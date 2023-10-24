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

brasil=df.loc['Brasil',anos]

print(brasil)

#Vamos criar um dataframe com as informaçoes da variavel brasil

#primeito vamos criar um dicionario com os dados

brasil_dicio={'ano': brasil.index.tolist(),'imigrantes': brasil.values.tolist()} # tolist para criar a lista

print(brasil_dicio)

dados_brasil=pd.DataFrame(brasil_dicio)

print(dados_brasil)

# VAMOS fazer dois gráficos ao mesmo tempo usando fig,axs

import matplotlib.pyplot as plt

fig,axs = plt.subplots(1,2,figsize=(12,5)) # Colocamos 1, 2 para dizermos qye serao dois gráficos

axs[0].plot(dados_brasil['ano'],dados_brasil['imigrantes']) # dados dos gráfico

axs[0].set_title('Imigração do Brasil para o canadá \n Entres os anos de 1980 a 2013')
axs[0].set_xlabel('Anos')# Rótulos da gráfico horizontal
axs[0].set_ylabel('Quant. de Imigrantes')# Rótulos do gráfico vertical

axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))## vamos mostrar de 5 em 5 anos para nãoficar muito amontoado
axs[0].grid()

# Dados do segnndo gráfico
axs[1].boxplot(dados_brasil['imigrantes']) # Apenas dados numericos

axs[1].set_title('Imigração do Brasil para o canadá \n Entres os anos de 1980 a 2013')
axs[1].set_xlabel('Anos')# Rótulos da gráfico horizontal
axs[1].set_ylabel('Quant. de Imigrantes')# Rótulos do gráfico vertical

axs[1].xaxis.set_major_locator(plt.MultipleLocator(5))## vamos mostrar de 5 em 5 anos para nãoficar muito amontoado
axs[1].grid()

plt.show()

print(dados_brasil.describe())





