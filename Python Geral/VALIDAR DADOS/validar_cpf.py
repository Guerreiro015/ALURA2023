from validate_docbr import CPF

class validar_cpf:
  def __init__(self,documento):
    documento=str(documento)
    if self.cpf_analise(documento):
      self.cpf = documento
      
      self.formatar() 
    else:
      print("CPF Inválido")
      

  def cpf_analise(self,documento):
    
    if len(documento) == 11:
      validador = CPF()
      return validador.validate(documento)
    
    else:    
      return False
  def formatar(self):
      # f=self.cpf[0:3]
      # f1=self.cpf[3:6]
      # f2=self.cpf[6:9]
      # f3=self.cpf[9:]

      mascara = CPF()
      mascara =  mascara.mask(self.cpf)

      #print(f"CPF :  {f}.{f1}.{f2}-{f3} validado com Sucesso")
      print(f"CPF : {mascara} validado com Sucesso")
  # def __str__(self):
  #   return self.formatar()
    
