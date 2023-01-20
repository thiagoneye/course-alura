"""
01.
02.
03.
04. 
05. Usando Propriedades
"""

# Classes

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


# Main

cliente = Cliente('nico')
print(cliente._Cliente__nome)
print(cliente.nome)

cliente.nome = "marco"
print(cliente._Cliente__nome)
print(cliente.nome)
