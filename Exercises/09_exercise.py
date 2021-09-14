taxa = float(input('Digite o preço da sua hora de trabalho: '))
horas_trabalhadas = int(input('Digite quantas horas foram trabalhadas: '))

valor_a_pagar = horas_trabalhadas * taxa

print(f'Você irá receber {valor_a_pagar:.2f}R$')
