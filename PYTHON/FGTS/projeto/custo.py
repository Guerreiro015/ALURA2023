# PROGRAMA PARA CALULAR OS CUSTO DAS FOLHAS MENSAL

import os
os.system("cls" or None)

import pandas as pd

abrir = input("Digite o nome do arquivo origem. : ").upper()
novo = input("Digite o nome do arquivo a ser criado. : ").upper()
abrir = (abrir+".xlsx")
novo_arquivo = (novo+".xlsx")


tb = pd.read_excel(abrir)
print(tb[["Id Contratado","Nome","Cargo"]]) # para selecionar os campos para ver usas colchetes duplos
 


#INSERIR UMA COLUNA Ref. aos sidicatos usando Parametros ( nº coluna,nome coluna, valor da coluna)
tb.insert(7,"Selur", tb["4Salário - Mensalistas"]*0.5/100)
tb.insert(7,"Steriiisp", 0)
tb.insert(7,"Siemaco", 0)


# Calcular valors dos sindicatos
tb.loc[tb["Sindicatos"] == "SIEMACO SAO PAULO LIMP URBANA","Siemaco"] = tb["4Salário - Mensalistas"]*0.6/100

tb.loc[tb["Sindicatos"] == "SIND TRAB EMP DE ONIBUS RODOV INTEREST INTERM SET DIF SAO PAULO","Steriiisp"] = tb["4Salário - Mensalistas"]*0.4/100

# criar colunas se elas não existirem
campos = tb.columns
if "1001Base INSS 13º Salário" not in campos:
    tb.insert(10,"1001Base INSS 13º Salário", 0)

if "1007Base do INSS Normal" not in campos:
    tb.insert(10,"1007Base do INSS Normal", 0)

if "1008Base do INSS Normal Excedente" not in campos:
    tb.insert(10,"1008Base do INSS Normal Excedente", 0)

if "1031Base INSS/FGTS Férias do Mês" not in campos:
    tb.insert(10,"1031Base INSS/FGTS Férias do Mês", 0)


if "1005Base do FGTS Normal" not in campos:
    tb.insert(10,"1005Base do FGTS Normal", 0)

if "1010Base do FGTS 13º Salário" not in campos:
    tb.insert(10,"1010Base do FGTS 13º Salário", 0)

if "1031Base INSS/FGTS Férias do Mês" not in campos:
    tb.insert(10,"1031Base INSS/FGTS Férias do Mês", 0)

if "1039Valor do FGTS - GRFF" not in campos:
    tb.insert(10,"1039Valor do FGTS - GRFF", 0)


if "953Dif Salário Aprendiz - Mensalistas" not in campos:
    tb.insert(10,"953Dif Salário Aprendiz - Mensalistas", 0)




# Calcular valOres dos INSS
tb.insert(10,"Inss",(tb["1001Base INSS 13º Salário"]+tb["1007Base do INSS Normal"]+tb["1008Base do INSS Normal Excedente"]+tb["1031Base INSS/FGTS Férias do Mês"])*28.9854/100)

# Calcular valOres dos FGTS
tb.insert(10,"Fgts",(tb["1005Base do FGTS Normal"]+tb["1010Base do FGTS 13º Salário"]+tb["1031Base INSS/FGTS Férias do Mês"])*8/100-tb["1039Valor do FGTS - GRFF"])

# Ajustando valOres dos FGTS dos jovens aprendizes
tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","Fgts"] = tb["1005Base do FGTS Normal"]*2/100

# Zerando o INSS das licenças maternidadees
if "7Salário-Maternidade" in campos:
    tb.loc[tb["Situação"] == "Licença-Maternidade","Inss"] = 0



# Salvando o arquivo criado
tb.to_excel(novo_arquivo,index=False)

nova = pd.read_excel(novo_arquivo)
print("\n------  Montagem da Planilha de custos Mensais Feito com Sucesso e OK.....  \n")
