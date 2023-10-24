import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt


cores = []

df = pd.read_csv('imigrantes.csv')
#print(df)


df.set_index('País',inplace=True) # Colocar o culuna pais como indice
#print(df)


anos=list(map(str,range(1980,2014))) #Criando uma lista  de anos
#print(anos)

america_sul = df.query('Região == "América do Sul"')
#print(america_sul)

america_sul=america_sul.sort_values('Total',ascending=True) #Ordenando do menor pro maior

# Vamos criar gráficos de barras
for i in america_sul.index:
    cores.append('green') if i == 'Brasil' else cores.append('silver')

fig,ax = plt.subplots(figsize=(10,5))
ax.barh(america_sul.index,america_sul['Total'],color=cores) #se mudarmos de bar para BARH - Invertemos o gráfico
ax.set_title('Imigrações da América do Sul para o Canadá entre 1980 e 2013\nBRASIL Está em 4º Lugar',color='red',fontsize=16,loc='left')
ax.set_ylabel('Paises da America',fontsize=14,color='blue')
ax.set_xlabel('Números de Imigrantes',fontsize=16,color='g')
ax.xaxis.set_tick_params(labelsize=8) #Tamanho da letra do eixo
ax.yaxis.set_tick_params(labelsize=10) #Tamanho da letra do eixo

# Mostrar os valores totais de cada item país
for i, v in enumerate(america_sul['Total']):
    ax.text(v + 20, i, str(f'{v:,.0f}'), color='blue', fontsize=10, ha='left', va='center')

ax.set_frame_on(False) # Esconder as bordas
ax.get_xaxis().set_visible(False) # Esconder os valores do eixo x horozontal
#ax.tick_params(axis='both', witch='both', length=0)# Esconder marcações dos gráficos verticais

fig.savefig('America.png',transparent=False,dpi=300, bbox_inches='tight')

plt.show()
