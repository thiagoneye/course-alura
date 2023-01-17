"""
01. O problema do paradigma procedual.
"""

# Functions

def cria_conta(numero, titular, saldo, limite):
    return {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'O saldo da conta é de R$ {conta["saldo"]}.')

# Main

conta = cria_conta(123, "Nico", 55.0, 1000.0)
deposita(conta, 300.0)
extrato(conta)
saca(conta, 100.0)
extrato(conta)
