import os
os.system('cls')
#pip install validate-docbr
from validar_cnpj import *

from validate_docbr import CPF,CNPJ


#cpf = input('Por favor digite o CPF: ')
cnpj=33572312000129
cnpj1=35379838000112
cnpj2='00360305000104'
cnpj3=111222333
cnpj4 = 111222333444555
cnpjs = [cnpj,cnpj1,cnpj2,cnpj3,cnpj4]
for i in cnpjs:

    validar_cnpj(i)


#usando o pacote manual
# cpf = CPF()
# print(cpf.validate('31375855385'))


# fatiamento simples
# f=cpf[0:3]
# f1=cpf[3:6]
# f2=cpf[6:9]
# f3=cpf[9:]
# print(f,f1,f2,f3)
