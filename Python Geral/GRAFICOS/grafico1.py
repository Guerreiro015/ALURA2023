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

import matplotlib.pyplot as plt


plt.figure(figsize=(8,4)) # define o tamanho do gráfico ( Opcional)
plt.plot(dados_brasil['ano'],dados_brasil['imigrantes']) # dados dos gráfico
# vamos mostrar de 5 em 5 anos para nãoficar muito amontoado
plt.title('Imigração do Brasil para o Canadá\n Entre 1980 e 2013')# Título do gráfico
plt.xlabel('Anos')# Rótulos da gráfico horizontal
plt.ylabel('Quant. de Imigrantes')# Rótulos do gráfico vertical

plt.xticks(['1980','1985','1990','1995','2000','2005','2010','2013'])
plt.yticks([500, 1000, 1500, 2000, 2500, 3000]) # Valores sem aspas

plt.show()





