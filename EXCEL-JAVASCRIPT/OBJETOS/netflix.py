class cliente:
    import os
    os.system("cls")
    def __init__(self,nome,email,plano):
        self.nome = nome
        self.email = email
        self.listas_planos = ["basic","premium","top"]
        if plano in self.listas_planos:
            self.plano = plano
        else:
            print("Plano invalido")
        self.valor = 0

    
    def mudar_plano(self,novo_plano):   
        if novo_plano in self.listas_planos:
            self.plano = novo_plano
            print(f" o cliente {self.nome} mudou para o plano {self.plano}")
        else:
            print("Não foi possível alterar o plano, nome do plano não é válido")    


    def filmes(self,filme,plano):
        if plano == cliente01.plano or cliente01.plano == self.listas_planos[2]:
            print(f"O cliente {self.nome} Pode assistir o filme - { filme} - \n")

        else:
            print(f"O cliente {self.nome} Nâo pode assistir o filme - {filme} - Precisa alterar o plano\n")


cliente01 = cliente("antonio","antonio@email","basic")
print(cliente01.nome)
print(cliente01.plano)

print(f" O cliente {cliente01.nome} foi cadastrado com sucesso no plano {cliente01.plano}\n")

cliente01.filmes("Amor De Noite","top")

cliente01.mudar_plano("premium")

print(f"\n O Novo plano do {cliente01.nome} e o plano {cliente01.plano}\n")

cliente01.filmes("Amor De Noite","premium")








        