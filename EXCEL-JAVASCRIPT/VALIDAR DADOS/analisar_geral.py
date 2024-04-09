import os
os.system('cls')
#pip install validate-docbr
from validar_cpf import *
from VALIDACAO_CPF_CNPJ import *



#cpf = input('Por favor digite o CPF: ')
cpf=12345678901
cpf1=15316264754
cpf2=31375855387
cpf3=111222333
cpf4=111222333444555
cnpj=33572312000129
cnpj1=35379838000112
cnpj2='00360305000104'
cnpj3=111222333
cnpj4 = 111222333444555
cpfs = [cpf,cpf1,cpf2,cpf3,cpf4,cnpj,cnpj1,cnpj2,cnpj3,cnpj4]
for i in cpfs:

    validar_geral(i)

#<<<<<<<<<>>>>>>>>>>

print('\n')
dados=[
12345678901,
15316264754,
31375855387,
111222333,
111222333444555,
33572312000129,
35379838000112,
'00360305000104',
111222333,
111222333444555]

for i in dados:
    validar_geral(i)