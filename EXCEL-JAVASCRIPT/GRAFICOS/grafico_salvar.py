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

# VAMOS USAR O PARAMETRO FIG, AX


fig,ax = plt.subplots(figsize=(8,4))
#------------------------------------------------------
print(fig.canvas.get_supported_filetypes())# mostrar os modos que pode salvar um gráfico
#---------------------------------------------------
ax.plot(dados_brasil['ano'],dados_brasil['imigrantes'],lw=3,color='Red') # dados dos gráfico
ax.set_title('Imigração do Brasil para o canadá \n Entres os anos de 1980 a 2013',color='Blue')
ax.set_xlabel('Anos',color='Green',fontsize=14)# Rótulos da gráfico horizontal
ax.set_ylabel('Quant. de Imigrantes',color='green',fontsize=16)# Rótulos do gráfico vertical

ax.xaxis.set_major_locator(plt.MultipleLocator(5))## vamos mostrar de 5 em 5 anos para nãoficar muito amontoado

ax.spines['top'].set_visible(False) # Retirar linha de cima
ax.spines['right'].set_visible(False) # Retirar linha da direita

#Salvando o gráfico

fig.savefig('Imigrantes.png',transparent=False,dpi=300, bbox_inches='tight')

plt.show()





