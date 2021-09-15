velocidade = float(input('Informe a velocidade: '))

if velocidade > 80:
  diferenca = velocidade - 80
  valor = diferenca * 5
  print(f'Você foi multado em: R$ {valor:.2f}')
