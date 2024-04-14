class Hotel():
    lista_clientes=[]
    def __init__(self,cliente,quarto,cafe=None,almoco=None,janta=None):
        self._cliente=cliente
        self._quarto=quarto
        self._almoco=almoco
        self._cafe=cafe
        self._janta=janta        
        Hotel.lista_clientes.append(self)
        

    def __str__(self):
        if self._cafe==None:
            self._cafe=0.0
        if self._almoco==None:
            self._almoco=0.0
        if self._janta==None:
            self._janta=0.0

    def mostrar():
     for i in Hotel.lista_clientes:
        if i._cafe==None:
            i._cafe=0.0
        if i._almoco==None:
            i._almoco=0.0
        if i._janta==None:
            i._janta=0.0
        print( f'\nO Cliente {i._cliente} está no quarto {i._quarto}\n{"Gastos:".upper()} de {i._cliente} \n R$: {i._cafe: .2f} de cafe \n R$: {i._almoco: .2f} de almoco\n R$: {i._janta: .2f} de Janta')
    


   
