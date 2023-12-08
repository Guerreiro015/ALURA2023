
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

verba1005=1005
verba1010=1010
verba1031=1031
verba1039=1039
 
 

tb = pd.read_excel("minha base.xlsx",sheet_name="base")

# campos = tb.columns
# if "1001Base INSS 13º Salário" not in campos:
#     tb.insert(10,"Jovem", 0)

# if tb['Cargo']=="MENOR/JOVEM APRENDIZ":
#     tb['Jovem']=


v1005=tb['a1005'].sum()
v1010=tb['1010'].sum()
v1031=tb['1031'].sum()
v1039=tb['1039'].sum()


print(f'Valor da verba 1005: {v1005: ,.2f}')
print(f'Valor da verba 1010: {v1010: ,.2f}')
print(f'Valor da verba 1031: {v1031: ,.2f}')
print(f'Valor da verba 1039: {v1039: ,.2f}')

