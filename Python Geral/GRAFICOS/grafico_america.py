import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
# IPython_default = plt.rcParams.copy()
# plt.style.use('fivethirtyeight')
cores = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']

df = pd.read_csv('imigrantes.csv')
print(df)


df.set_index('País',inplace=True) # Colocar o culuna pais como indice
print(df)


anos=list(map(str,range(1980,2014))) 
print(anos)

america_sul = df.query('Região == "América do Sul"')
print(america_sul)


# Vamos criar gráficos de barras

fig,ax = plt.subplots(figsize=(12,5))
ax.bar(america_sul.index,america_sul['Total'],color=cores)
ax.set_title('Imigração da America para o Canadá\nEntre 1980 e 2013',color=cores[4],fontsize=16,loc='left')
ax.set_xlabel('Paises da America',fontsize=14,color='blue')
ax.set_ylabel('Números de Imigrantes',fontsize=14)
ax.xaxis.set_tick_params(labelsize=8) #Tamanho da letra do eixo
ax.yaxis.set_tick_params(labelsize=10) #Tamanho da letra do eixo


plt.show()
