
from validate_docbr import CPF,CNPJ

class validar_geral:
  def __init__(self,documento):
    self.documento = str(documento)
    if len(self.documento) == 11:
      validar_cpf(self.documento)
    elif len(self.documento) == 14:
      validar_cnpj(self.documento)
    else:
      print("Numeros de caracteres inválidos")

class validar_cpf:
  def __init__(self,documento):
    self.documento=str(documento)
    if self.cpf_analise(self.documento):
      self.cpf = self.documento
      
      self.formatar() 
    else:
      print("CPF Inválido")
      

  def cpf_analise(self,documento):
    
    if len(self.documento) == 11:
      validador = CPF()
      return validador.validate(self.documento)
    
    else:    
      return False
  def formatar(self):
      # f=self.cpf[0:3]
      # f1=self.cpf[3:6]
      # f2=self.cpf[6:9]
      # f3=self.cpf[9:]
      # print(f"CPF :  {f}.{f1}.{f2}-{f3} validado com Sucesso")

      self.mascara = CPF()
      self.mascara =  self.mascara.mask(self.cpf)

      print(f"CPF : {self.mascara} validado com Sucesso")
  # def __str__(self):
  #   return self.formatar()
    

class validar_cnpj:
  def __init__(self,documento):
    self.documento=str(documento)
    if self.cnpj_analise(self.documento):
      self.cnpj = self.documento
      
      self.formatar() 
    else:
      print("CNPJ Inválido")
      
  def __str__(self):
    if self.cnpj_analise(self.documento): 
      print(f"CNPJ : {self.mascara} validado com Sucesso")

  def cnpj_analise(self,documento):
    
    if len(self.documento) == 14:
      validador = CNPJ()
      return validador.validate(self.documento)
    
    else:    
      return False
  def formatar(self):
      
      self.mascara = CNPJ()
      self.mascara =  self.mascara.mask(self.cnpj)
      print(f"CNPJ : {self.mascara} validado com Sucesso")
      
      