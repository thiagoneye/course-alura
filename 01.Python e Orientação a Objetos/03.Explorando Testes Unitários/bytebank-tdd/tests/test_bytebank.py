from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    # Given-When-Then
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-Ação

        assert resultado == esperado # Then-Desfecho

    def test_quando_nome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    #@mark.skip(reason='Não quero executar isso agora.')
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
    """
    def test_quando_chamado_retorna_string_str(self):
        entrada_nome = 'Teste'
        entrada_data = '12/03/2000'
        entrada_salario = 1000

        esperado = f'Funcionario({entrada_nome}, {entrada_data}, {entrada_salario})'

        funcionario_teste = Funcionario(entrada_nome, entrada_data, entrada_salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado
    """
