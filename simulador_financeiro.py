def simular_emprestimo(valor, taxa, meses):
    juros = valor * (taxa/100) * meses
    total = valor + juros
    return round(total,2)
