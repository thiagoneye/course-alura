"""
01.
02. Classes e Objetos
03. Usando Métodos
04. Encapsulamento
05.
06. Métodos Privados e Estáticos
"""

# Classes

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O saldo do titular {self.__titular} é de R$ {self.__saldo}.')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        return valor <= self.__saldo + self.__limite

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor é superior ao limite permitido.')

    def transfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


# Main

conta1 = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)

print(f'O saldo da conta 1 é de R$ {conta1._Conta__saldo}.')
conta1.extrato()

conta1.saca(1200)
conta2.saca(200)
