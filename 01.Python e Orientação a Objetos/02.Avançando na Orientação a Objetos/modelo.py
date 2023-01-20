"""
1. Relembrando Classes e Objetos
"""

# Classes

class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


# Main

def __init__(self):    
    vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
    print(vingadores.nome)

    atlanta = Serie('Atlanta', 2018, 2)
    print(f'Nome: {atlanta.nome}')
    print(f'Ano: {atlanta.ano}')
    print(f'Temporada: {atlanta.temporadas}')
