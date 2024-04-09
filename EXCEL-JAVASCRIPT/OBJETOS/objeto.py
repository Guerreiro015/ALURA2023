import os
os.system("cls")

from dados_objeto import cria_conta, deposita, saca, extrato
conta1 = cria_conta(111, "Antonio", 55.0, 1000.0)
conta2 = cria_conta(222,"LUCAS",855,600)

extrato(conta1)
deposita(conta1, 78.0)
extrato(conta1)
saca(conta1, 26.0)
extrato(conta1)

extrato(conta2)
deposita(conta2,45)
extrato(conta2)
saca(conta2,540)
extrato(conta2)








