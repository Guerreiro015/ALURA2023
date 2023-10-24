import os
os.system('cls')
#print("\033[1;33;0m ola mundo")

print("\33[33m="*50)
print("-"*50)
print("\33[1;34mCÁLCULO DE INSS - FGTS - IRRF ".center(50))
print("\033[33m-"*50)
print("="*50)
sal=input('\033[32mDigite o valor do Salário........ ..: ')
if sal == "":
  sal=0
sal=int(sal)
fal=input('Digite Valor das faltas e atrasos. .: ')
if fal == "":
  fal=0
fal=int(fal)
pen=input('Digite o valor da Pensão............: ')
if pen == "":
  pen=0
pen=int(pen)
dep=input('Digite a Quant. de Dependentes. IR..: ')
if dep == "":
  dep=0
dep=int(dep)

  
print(sal,fal,pen,dep)

tetoinss = 876.95
dep=dep*189.59
deducao_simplicada = 528.00

#------------------------------------------------------------
basesalario = [0,1320, 2571.29, 3856.94, 7507.49]

aliquotainss = [7.5, 9, 12, 14]

deducaoinss = [0, 19.8, 96.94, 174.08]

#-----------------------------------------------------
baseir = [2112.01, 2826.66, 3751.06, 4664.68,5000000]

aliquotair = [0,7.5, 15, 22.5, 27.5]

parceladeduzir = [0,158.4, 370.4, 651.73, 884.96]

deducaodependenteir = 189.59

valordeducaoir = deducaodependenteir*dep

#------------------------------------------------------------
sal=(sal-fal)
fgts=sal*0.08
if fgts <=0:
   fgts=0
inss=0
cont = 0


for i in range(cont,len(basesalario)):
      if sal > basesalario[4]:
        inss = tetoinss
        break
      
      if (sal > basesalario[cont] and sal < basesalario[cont+1]):
        inss = (sal*(aliquotainss[cont]/100))-deducaoinss[cont]
        break
      else:
        cont = cont+1

print("\33[33m="*50)
print(f'\033[36mValor base do INSS é  : {sal:,.2f}')
print(f'O valor do INSS será..: {inss:,.2f}')
print("\33[33m="*50)
#--------------------------------------------------------
#--------------------------------------------------------

base_deducao_ir = (pen+dep+inss)
cont = 0
for i in range(cont,len(baseir)):
  if (base_deducao_ir < deducao_simplicada):
          base_deducao_ir = deducao_simplicada
    
  salarioir=sal-base_deducao_ir
  if salarioir <= 0:
    salarioir = 0

  if salarioir<baseir[0]:
    ir=0
    break
  
  if salarioir < baseir[cont]:
    ir=(salarioir*(aliquotair[cont]/100)) - parceladeduzir[cont]
    break
  else:
    cont=cont+1


print(f'\033[35mO Valor do FGTS é ....: {fgts:,.2f}')
print("\33[33m="*50)
print(f'\033[36mO Base do IRRF  é ....: {salarioir:,.2f}')
print(f'O valor do IRRF é ....: {ir:,.2f}')
print("\33[33m="*50)
fim = input("FIM")
print("\033[0;0;0m")

