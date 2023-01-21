"""
1. Relembrando Classes e Objetos
2. Removendo Duplicação com Herança
"""

# Classes

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


# Main

if __name__ == '__main__':
    vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)

    atlanta = Serie('Atlanta', 2018, 2)
    print(f'Nome: {atlanta.nome}')
    print(f'Ano: {atlanta.ano}')
    print(f'Temporada: {atlanta.temporadas}')

    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()

    print(f'Likes: {atlanta.likes}')
