from time import sleep


def menu(msg, lista, tam=0):
    tam += len(msg)
    sleep(2)
    print('*' * tam)
    print(msg)
    print('*' * tam)
    for i, c in enumerate(lista):
        print(f'{i + 1} - {c}')
    print('*' * tam)


def opcao_menu(msg):
    while True:
        try:
            opcao = int(input(msg))
            if opcao > 5:
                raise (opcao)
        except(ValueError, TypeError):
            if opcao >= 5:
                print('Opção indisponivel')
            else:
                print('Apenas numeros sao validos.')
            continue
        except(KeyboardInterrupt):
            print('\nSaindo do programa...')
            break
        else:
            if opcao > 0:
                return opcao
            else:
                print('Apenas numeros positivos.')
                continue


def validacao_valor(msg):
    while True:
        try:
            valor = int(input(msg))
        except(TypeError, ValueError):
            print('Apenas numeros sao permitidos. Tente Novamente!')
            continue
        except(KeyboardInterrupt):
            print('\nSaindo do programa...')
            break
        else:
            if valor > 0:
                return valor
            else:
                print('Apenas numeros positivos.')
                continue


class Conta:

    def __init__(self, numero_conta, titular, saldo, limite):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def numero_conta(self):
        return self.__numero_conta


    @property
    def saldo(self):
        return f'{self.__saldo:.2f}'

    @property
    def limite(self):
        return f'{self.__limite:.2f}'

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite


    def extrato(self):
        print('Retirando extrato da conta, Aguarde um momento...')
        sleep(1)
        resultado = ''
        contas = {
            "Conta": self.__numero_conta,
            "Titular": self.titular,
            "Saldo": self.saldo,
            "Limite": self.limite
        }
        print('** Extrato **')
        for index, (key, value) in enumerate(contas.items()):
            resultado += f'{index + 1} - {key}: {value}\n'
        print(resultado, end='')

    def saca(self, valor):
        if valor > self.__saldo:
            print('Saldo da conta insuficiente!')
        else:
            self.__saldo -= valor
            print('Saque feito com sucesso!')

    def deposita(self, valor):
        if valor < self.__limite:
            self.__saldo += valor
            print('Deposito feito com sucesso!')
        else:
            print('Valor excedeu o limite da conta!')

    def transfere(self, valor, destino):
        if self.__numero_conta == destino.__numero_conta or self.__saldo < valor:
            print('Transferancia Invalida!')
        else:
            try:
                self.saca(valor)
                destino.deposita(valor)
            except:
                print('Erro ao tentar transferir de uma conta para outra')
            else:
                self.extrato()
                destino.extrato()
                print('Deposito feito com sucesso!')


conta1 = Conta(123, 'douglas', 5000, 20000)
conta2 = Conta(456, 'deise', 2500, 20000)
conta3 = Conta(564, 'julia', 3500, 20000)
conta4 = Conta(234, 'roselaine', 8000, 20000)
conta5 = Conta(489, 'diego', 10000, 20000)
conta6 = Conta(321, 'rodrigo', 5600, 20000)
opc = 0
contas = [conta1, conta2, conta3, conta4, conta5, conta6]

while opc != 5:
    menu('Banco Central', ['Extrato', 'Deposito', 'Saque', 'Transferir', 'Sair'])
    opc = opcao_menu('Digite sua opção: ')
    if opc:
        if opc == 1:
            conta1.extrato()
        elif opc == 2:
            valor = validacao_valor('Digite o valor que deseja deposita:  R$')
            if valor:
                conta1.deposita(valor)
            else:
                break
        elif opc == 3:
            valor = validacao_valor('Digite o valor que deseja sacar:  R$')
            if valor:
                conta1.saca(valor)
            else:
                break
        elif opc == 4:
            valor = validacao_valor('Digite o valor que queira transferir: R$')
            titular = input('Digite o nome do titular para quem queira transferir: ').title()
            if valor:
                for cont in contas:
                    if cont.titular == titular:
                        conta1.transfere(valor, cont)
                        break
            else:
                break
        else:
            print('Saindo...')
    else:
        break
