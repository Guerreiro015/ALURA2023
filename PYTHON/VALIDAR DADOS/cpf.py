import os
os.system('cls')
#pip install validate-docbr
from validar_cpf import *

from validate_docbr import CPF


#cpf = input('Por favor digite o CPF: ')
cpf=12345678901
cpf1=15316264754
cpf2=31375855387
cpf3=111222333
cpf4 = 111222333444555
cpfs = [cpf,cpf1,cpf2,cpf3,cpf4]
for i in cpfs:

    validar_cpf(i)


#usando o pacote manual
# cpf = CPF()
# print(cpf.validate('31375855385'))


# fatiamento simples
# f=cpf[0:3]
# f1=cpf[3:6]
# f2=cpf[6:9]
# f3=cpf[9:]
# print(f,f1,f2,f3)
