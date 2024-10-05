from functools import reduce

def calcula_saldo(lancamentos):
    # Usa map para transformar os lançamentos em valores positivos ou negativos (crédito ou débito)
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    # Usa reduce para somar todos os valores e calcular o saldo final
    saldo_final = reduce(lambda acc, valor: acc + valor, valores)
    
    return saldo_final
