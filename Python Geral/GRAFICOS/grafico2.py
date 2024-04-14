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

paises=df.loc[['Brasil','Argentina','Cuba','Peru'],anos] #Vamos usar dois paises

paises=paises.T # Trocar horizontal por vertical

print(paises)

# VAMOS USAR MAIS DE UMA INFORMAÇÃO
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4)) # define o tamanho do gráfico ( Opcional) em polegadas
plt.plot(paises['Brasil'],label='Brasil')
plt.plot(paises['Argentina'],label='Argentina')
plt.plot(paises['Cuba'],label='Cuba')
plt.plot(paises['Peru'],label='Peru')

plt.title('Imigração do Brasil, Argentina, Cuba e Peru para o Canadá\n Entre os anos de 1980 e 2013')# Título do gráfico

plt.xlabel('Anos')# Rótulos da gráfico horizontal
plt.ylabel('Quant. de Imigrantes')# Rótulos do gráfico vertical

plt.xticks(['1980','1985','1990','1995','2000','2005','2010','2013'])
#plt.yticks([1000, 2000, 3000, 4000, 5000, 6000,7000]) # Valores sem aspas

plt.legend()
plt.show()





