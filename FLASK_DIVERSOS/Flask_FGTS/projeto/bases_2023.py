

bases_inss = [1320,2571.29,3856.94,7507.49]
aliqinss = [7.5,9.0,12,14]
desc = [0,19.8,96.94,174.08,876.95]
teto_inss = 876.95



bases_irrf = [2112,2826.65,3751.05,4664.68,9999999999]
aliqir =    [0,7.5,15, 22.5,27.5]
desc_ir = [0,158.4,370.4,651.73,884.96]

dependente = 189.79
deducao_simplicada = 528.00



valor_inss=0
global x
x=0
def inss(valor):
    x=0
    for i in bases_inss:
        if valor > bases_inss[3]:
          valor_inss = teto_inss
          return valor_inss
        else:
          if valor <= i:
            valor_inss = (valor*aliqinss[x]/100)-(desc[x])
            return valor_inss
            
          else:
            x += 1
            
#print(f'{inss(3000): .2f} ' )          
        
def irrf(valor):
  x=0
  for i in bases_irrf:
      if valor <= i:
         valor_irrf = (valor*aliqir[x]/100)-desc_ir[x]        
         return valor_irrf
      else:
       x += 1         

#print(f'{irrf(6000): .2f} ' )          

