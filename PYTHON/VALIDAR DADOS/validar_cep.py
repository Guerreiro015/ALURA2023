import requests
class cep:
    def __init__(self,valor):
        cep = str(valor)
        if self.valida_endereco(cep):
            self.cep = cep
            # parte1 = self.cep [:5]
            # parte2 = self.cep [5:]
            # print (f'CEP: {parte1}-{parte2} -  Validado foi Com Sucesso')
            print( self.solicitação())
        else:
            print(f"Número de CEP {cep} é Inválido")
            raise ValueError('Valor digitado não pode ser um CEP')
        
    def __str__(self):

        return self.formato_cep()
    
    def valida_endereco(self,valor):
        return True if len(valor) == 8 else False
        
    def formato_cep(self):
        parte1 = self.cep [:5]
        parte2 = self.cep [5:]
        return f'CEP: {parte1}-{parte2} -  Validado Com Sucesso'
    
    def solicitação(self):
            r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
            return r.json