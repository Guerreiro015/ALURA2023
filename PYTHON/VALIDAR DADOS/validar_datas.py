from datetime import datetime,timedelta

class data_br:
    def __init__(self):
        self.momento = datetime.today()

    def __str__(self):
        return self.dia_cadastro()
        
                
       
    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        self.mes = meses_do_ano[self.momento.month-1]# NÃO precisa parenteses
        return self.mes
    
    def dia_cadastro(self):
        dia_semana = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        self.dia = dia_semana[self.momento.weekday()]# precisa parenteses
        
        return self.dia
    
    def data_formatada(self):
        self.forma_data = self.momento.strftime(("%d/%m/%Y"))
        self.forma_hora = self.momento.strftime((" %H:%M"))

        return self.forma_data, self.forma_hora
    
    def tempo(self):
        tempo = (datetime.today()+timedelta(days=30,hours=10)) - datetime.today()
        return tempo
    