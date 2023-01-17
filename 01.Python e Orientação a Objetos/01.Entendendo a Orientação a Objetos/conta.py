"""
02. Classes e Objetos.
03. Usando Métodos.
"""

# Classes

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O saldo do titular {self.titular} é de R$ {self.saldo}.')

# Main

conta1 = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)

print(f'O saldo da conta 1 é de R$ {conta1.saldo}.')
conta1.extrato()
