class conta:

    def __init__(self, numero, titular, saldo, usadas):

        print(f"Construindo objeto ...{self}\n")

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__usadas = 0

    def deposita(self, valor):
        self.__saldo += valor
    

    def milhas_utilizadas(self,valor):
        self.__saldo -= valor
        self.__usadas += valor
    
    def extrato(self):
        print(f"O cliente {self.__titular} utilizou {self.__usadas} milhas \n")
        print(f"Saldo de milhas do {self.__titular} é {self.__saldo}\n")
    
    


    
    