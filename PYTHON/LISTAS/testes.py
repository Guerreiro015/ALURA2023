import os
os.system("cls")

class ContaSalario: 
  def __init__(self, codigo):
      self.codigo = codigo
      self._saldo = 0


  def __eq__(self,segundo):
      return self.codigo == segundo.codigo


ana=ContaSalario("ana")
pedro = ContaSalario("ana")
print(ana)
print(pedro)
print(ana == pedro)


