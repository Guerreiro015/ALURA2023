# import re

# class validar_tel:
#     def __init__(self,telefone):
#      self.telefone = telefone
#      if self.validar(self.telefone):
#       print(f'Telefone {self.telefone} validado com sucesso')
#      else:
#       print(f' Número de telefone inválido')

#     def validar(self,valor):
#         padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#        # padrao = "[0-9]{11}"
#         resposta = re.findall(padrao,valor)
#         print(padrao)
#         if resposta:
#             return True
#         else:
#             return False

import re

class TelefonesBr:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        print(f'Telefone {self.format_numero()} validado com sucesso')
        return self.format_numero()

    def valida_telefone(self,telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado