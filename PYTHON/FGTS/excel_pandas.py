
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
 
 

tabela = pd.read_excel("BASE.xlsx")

fgts=tabela.loc[tabela['Verba']==1005, 'Valor da Verba'].sum()

print(fgts)

