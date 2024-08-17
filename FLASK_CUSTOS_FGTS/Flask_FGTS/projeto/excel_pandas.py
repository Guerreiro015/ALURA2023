
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

verba1005='Base do FGTS Normal'
verba1010='Base do FGTS 13º Salário'
verba1031='Base INSS/FGTS Férias do Mês'
verba1039='Valor do FGTS - GRFF'
 
tb = pd.read_excel("minha base.xlsx",sheet_name="11_2023")


campos = tb.columns

if 'coluna' not in campos:
    tb.insert(4,"coluna", 0)
if "fgts_normal_jovem" not in campos:
    tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_normal_jovem"] = tb["Base do FGTS Normal"]
if "fgts_normal_jovem" not in campos:
    tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_13º_jovem"] = tb["Base do FGTS 13º Salário"]
if "fgts_normal_jovem" not in campos:
    tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_ferias_jovem"] = tb["Base INSS/FGTS Férias do Mês"]
if "fgts_normal_jovem" not in campos:
    tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_grrf_jovem"] = tb["Valor do FGTS - GRFF"]

v1005=tb['Base do FGTS Normal'].sum()
v1010=tb['Base do FGTS 13º Salário'].sum()
v1031=tb['Base INSS/FGTS Férias do Mês'].sum()
v1039=tb['Valor do FGTS - GRFF'].sum()
vcol=tb['coluna'].sum()


v1005j=tb['fgts_normal_jovem'].sum()
v1010j=tb['fgts_13º_jovem'].sum()
v1031j=tb['fgts_ferias_jovem'].sum()
v1039j=tb['fgts_grrf_jovem'].sum()

print(f'Valor da verba 1005: {v1005: ,.2f}')
print(f'Valor da verba 1010: {v1010: ,.2f}')
print(f'Valor da verba 1031: {v1031: ,.2f}')
print(f'Valor da verba 1039: {v1039: ,.2f}')
print(f'Valor da coluna nova: {vcol: ,.2f}' )


print(f'Valor da verba 1005 jovem: {v1005j: ,.2f}')
print(f'Valor da verba 1010 jovem: {v1010j: ,.2f}')
print(f'Valor da verba 1031 jovem: {v1031j: ,.2f}')
print(f'Valor da verba 1039 jovem: {v1039j: ,.2f}')

tb.to_excel("11_2023.xlsx",index=False)