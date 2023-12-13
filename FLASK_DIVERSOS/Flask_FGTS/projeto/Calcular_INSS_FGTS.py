
from flask import Flask, render_template, request, redirect, session,flash,send_from_directory
import mysql
from datetime import *
import time
import sqlite3
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
import pandas as pd

tb = pd.read_excel("minha base.xlsx")

from flask import Flask, render_template, request, redirect, session,flash,send_from_directory
import mysql
from datetime import *
import time
import sqlite3
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from bases_2023 import *
# pip install PyMySQL


app = Flask(__name__) #instanciando Flask  
app.secret_key = 'alura'


@app.route('/')
def index():
    
    tit="imposto de renda"
    return render_template('index.html')



@app.route('/calculo_inss')
def calculo_inss():    
    return render_template('calculo_inss.html')

#---------------------------------------------<>--------------------------------------------------   

@app.route('/calcular_inss', methods=['POST'])
def calcular_inss():
 
    salbase=float(request.form['salbase'])
    diastrab=float(request.form['diastrab'])
    hr50=float(request.form['hr50'])
    hr100=float(request.form['hr100'])
    adcnot=float(request.form['adcnot'])
    falta=float(request.form['falta'])
    dsr=float(request.form['dsr'])
    atrasos=float(request.form['atrasos'])
    depsf=float(request.form['depsf'])
    depir=float(request.form['depir'])
    opperic=(request.form['opperic'])
    opinsal=(request.form['opinsal'])
    insal=float(request.form['insal'])
    pensao=round(float(request.form['pensao']),2)
    salariominimo=1320
    salariofamilia=59.82
    tetosalariofailia=1754.18
    valorsalfam=round(depsf*salariofamilia,2)
    
    valordep=round(depir*189.59,2)
    deducaosimplificada=528
    
    if opinsal == 'sim':
        valor_insal=round((salariominimo*insal)/100,2)
    else: valor_insal=0

    if opperic == "sim" and opinsal == "nao":
        valor_peric=round((salbase*30/100),2)
    else: valor_peric = 0

    valorhora=salbase/220
    valorhora50=valorhora*1.5
    valorhora100=valorhora*2
    valoradcnot=valorhora*0.2
    

    valordia=salbase/30

    salario=round(valordia*diastrab,2)    
    horas50=round(hr50*valorhora50,2)
    horas100=round(hr100*valorhora100,2)
    adcnotur=round(adcnot*valoradcnot,2)
    somahoad = (horas100+horas50+adcnot)
    dsrhoad=round((somahoad)/25*5,2)

    valorfaltas=round(valordia*falta,2)
    valordsr=round(valordia*dsr,2)
    valoratrasos=round(valorhora*atrasos,2)

    bruto=round(salario + horas50 + horas100 + adcnotur+valor_insal+valor_peric+dsrhoad ,2)
    if bruto <= tetosalariofailia:       
        bruto += valorsalfam
    else:
        valorsalfam=0    
    descontos=round(valorfaltas+valordsr+valoratrasos,2)
    desc=round(valorfaltas+valordsr+valoratrasos+pensao,2)
    
    baseinss=round(bruto-descontos,2)
    basefgts=baseinss

    valorinss=round(inss(baseinss),2)
    if (valorinss+pensao+valordep) <= deducaosimplificada:
        descir=deducaosimplificada
    else:
        descir=(valorinss+pensao+valordep)

    baseir=round(baseinss-descir,2)
    if baseir <=0:
        baseir=0        

    valorirrf=round(irrf(baseir),2)
       
    valorfgts=baseinss*0.08
    valorfgts=round(valorfgts,2)
    
    dados={ 'desc': desc, 'dsrhoad': dsrhoad, 'salario': f'{salario: ,.2f}', 'bruto': f'{bruto: ,.2f}', 'insal': f'{valor_insal: ,.2f}', 'peric': f'{valor_peric: ,.2f}', 'valorsf': valorsalfam, 'valorhe50': horas50, 'valorhe100': horas100,'valoradcnot': adcnotur, 'valordsr': valordsr,'Faltas': valorfaltas,'Atrasos':valoratrasos,'baseinss': f'{baseinss: ,.2f}','valorinss':valorinss,'basefgts': f'{basefgts: ,.2f}','valorfgts': f'{valorfgts: .2f}', 'baseir':f'{baseir: ,.2f}', 'valorir':valorirrf,'valordep':valordep, 'pensao': pensao}

    print(valoratrasos)
    return render_template('mostrar_inss.html',dados=dados)       

#---------------------------------------------<>--------------------------------------------------   
#---------------------------------------------<>--------------------------------------------------   
@app.route('/encargos')
def encargos():
   return render_template('encargos_trabalhista.html')  

#---------------------------------------------<>--------------------------------------------------   

@app.route('/logout')
def logout():    
    flash('Usuário Desconectado')
    return redirect(url_for('login'))

#---------------------------------------------<>--------------------------------------------------   


#----------------< FGTS >------< FGTS >--------< FGTS >-------------------------------------------   


#---------------------------------------------<>--------------------------------------------------   

@app.route('/calculo_fgts')   
def calculo_fgts():
    
    return render_template('calculo_fgts.html')
  
@app.route('/calcular_fgts', methods=['POST'])
def calcular_fgts():
    mes=(request.form['mes'])
    ano=(request.form['ano'])    

    tb = pd.read_excel("minha base.xlsx",sheet_name=f'{mes}_{ano}')

    campos = tb.columns
    if "fgts_normal_jovem" not in campos:
        tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_normal_jovem"] = tb["Base do FGTS Normal"]
    if "fgts_normal_jovem" not in campos:
        tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_13º_jovem"] = tb["Base do FGTS 13º Salário"]
    if "fgts_normal_jovem" not in campos:
        tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_ferias_jovem"] = tb["Base INSS/FGTS Férias do Mês"]
    if "fgts_normal_jovem" not in campos:
         if "Valor do FGTS - GRFF" not in campos:
            tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_grrf_jovem"] = 0    
         else:
            tb.loc[tb["Cargo"] == "MENOR/JOVEM APRENDIZ","fgts_grrf_jovem"] = tb["Valor do FGTS - GRFF"]
    
    v1005=tb['Base do FGTS Normal'].sum()
    v1010=tb['Base do FGTS 13º Salário'].sum()
    v1031=tb['Base INSS/FGTS Férias do Mês'].sum()
    if "Valor do FGTS - GRFF" not in campos:
        v1039=0
    else:    
        v1039=tb['Valor do FGTS - GRFF'].sum()

    v1005j=tb['fgts_normal_jovem'].sum()
    v1010j=tb['fgts_13º_jovem'].sum()
    v1031j=tb['fgts_ferias_jovem'].sum()
    v1039j=tb['fgts_grrf_jovem'].sum()
    brutofgtsj=(v1005j+v1010j+v1031j)
    subtotalfgtsj=(brutofgtsj*2)/100
    totalfgtsj=subtotalfgtsj-v1039j

    v1005=v1005-v1005j
    v1010=v1010-v1010j
    v1031=v1031-v1031j
    v1039=v1039-v1039j
    brutofgts=(v1005+v1010+v1031)
    subtotalfgts=(brutofgts*8)/100
    totalfgts=subtotalfgts-v1039

    total_final=totalfgts+totalfgtsj



    
    dadosj={'verba1005j': f'{v1005j: ,.2f}', 'verba1010j': f'{v1010j: ,.2f}', 'verba1031j': f'{v1031j: ,.2f}', 'verba1039j': f'{v1039j: ,.2f}',
           'brutfgtsj': f'{brutofgtsj: ,.2f}','subfgtsj': f'{subtotalfgtsj: ,.2f}', 'totfgtsj': f'{totalfgtsj: ,.2f}'}
    
    dados={'verba1005': f'{v1005: ,.2f}', 'verba1010': f'{v1010: ,.2f}', 'verba1031': f'{v1031: ,.2f}', 'verba1039': f'{v1039: ,.2f}',
           'brutfgts': f'{brutofgts: ,.2f}','subfgts': f'{subtotalfgts: ,.2f}', 'totfgts': f'{totalfgts: ,.2f}', 'totfinal': f'{total_final: ,.2f}'}
    


#---------------------------------------------<>--------------------------------------------------   
    comp=f'Cálculo de FGTS - Competência {mes} / {ano}'
    return render_template('mostrar_fgts.html',dados=dados, comp=comp, dadosj=dadosj)    


<<<<<<< HEAD:FLASK DIVERSOS/Flask_FGTS/projeto/Calcular_INSS_FGTS.py
=======



>>>>>>> cbc76c5487fe20f8186245fbda6a8a1415a08424:FLASK_DIVERSOS/Flask_FGTS/projeto/Calcular_INSS_FGTS.py
app.run(debug=True)
#app.run(host='0.0.0.0', port=8080)
