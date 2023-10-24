class funci():
    def __init__(self,nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self,vendas):
        self.vendas = vendas

    def meta(self,meta):
        if self.vendas > meta:
            print(f" A meta do {self.nome}, era {meta} e o mesmo fez {self.vendas} então ele bateu meta")
        else:
             print(f" A meta do {self.nome}, era {meta} e o mesmo fez {self.vendas} então ele NÃO bateu meta")

vendedor0 = funci("Francisca")
vendedor0.vendeu(200)
vendedor0.meta(500)







