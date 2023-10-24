
import os
os.system("cls" or None)

import pandas as pd

# tabela = pd.read_excel("dados.xlsx")
# print(tabela.head())
# print(tabela)
# print(tabela["ID"])
# print(tabela["Nome"])

# #Alterar dados da planilha
# tabela.loc[tabela["ID"] == 112194,"Nome"] = "Antonio de Sousa Neto"
# print(tabela["Nome"],["ID"])

# #Salvar o arquivo em excel
# tabela.to_excel("dados2.xlsx",index=False)

# #+=============================================
# #Juntando duas planilhas
# df1 = pd.read_excel("dados.xlsx")
# df2 = pd.read_excel("dados2.xlsx")

# df3 = pd.concat([df1,df2])

# df3.to_excel("dados_juntos.xlsx")
# ##################################################

# # Puxando apenas alguas colunas de dados da planilha
# tabela = pd.read_excel("QUADRO GERAL.xlsx",sheet_name="QUADRO",usecols=(0,1,2,3))
# tabela.loc[tabela["Cargo"]=="BUEIRISTA","NOME"] = "Contratado para ser Bueirista"

tabela = pd.read_excel("QUADRO GERAL.xlsx",sheet_name="QUADRO")
print(tabela[["ID","NOME","SALARIO"]]) # para selecionar os campos para ver usas colchetes duplos
 
 #INSERIR UMA COLUNA NO FINAL DA PLANILHA DIRETO

tabela['TOTAL'] = tabela["SALARIO"]*tabela["DIAS"]

tabela['total3'] = tabela["SALARIO"]+tabela["DIAS"]

#INSERIR UMA COLUNA USANDO Parmetros .insert( nº coluna,nome coluna, valor da coluna)
tabela.insert(8,  "soma",  tabela["DIAS"]+tabela["DIAS"])  

tabela.to_excel("dados2.xlsx",index=False)

nova = pd.read_excel("dados2.xlsx")
print(nova[['NOME','Cargo','TOTAL','soma']])
