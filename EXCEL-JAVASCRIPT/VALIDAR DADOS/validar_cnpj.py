from validate_docbr import CPF,CNPJ

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
      
      