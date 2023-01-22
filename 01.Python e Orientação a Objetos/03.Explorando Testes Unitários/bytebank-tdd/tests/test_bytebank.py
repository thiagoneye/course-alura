from codigo.bytebank import Funcionario

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
