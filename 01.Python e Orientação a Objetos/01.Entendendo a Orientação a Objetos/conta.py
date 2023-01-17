"""
02. Classes e Objetos.
03. Usando Métodos.
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

    def sacar(self, valor):
        self.__saldo += valor


# Main

conta1 = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)

print(f'O saldo da conta 1 é de R$ {conta1._Conta__saldo}.')
conta1.extrato()
