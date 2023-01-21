"""
1. Relembrando Classes e Objetos
2. Removendo Duplicação com Herança
3. Reduzindo ifs com Polimorfismo
4. Quando Não Usar Herança
5. Duck Typing e um Modelo de Dados
"""

# Classes

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - Likes: {self._likes}'

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - Duração: {self.duracao} - Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


# Main

if __name__ == '__main__':
    vingadores = Filme('vingadores guerra infinita', 2018, 160)
    vingadores.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()

    atlanta = Serie('atlanta', 2018, 2)
    atlanta.dar_likes()
    atlanta.dar_likes()

    tmep = Filme('todo mundo em pânico', 1999, 100)
    tmep.dar_likes()

    demolidor = Serie('demolidor', 2016, 2)
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()

    filmes_e_series = [vingadores, atlanta, tmep, demolidor]
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    print(f'Tamanho da playlist: {playlist_fim_de_semana.tamanho} programas')
    print(f'Demolidor está na minha playlist? {demolidor in playlist_fim_de_semana}')

    for programa in playlist_fim_de_semana:
        print(programa)
