consumo_kWh = int(input('Digite a quantidade de kWh: '))

print('R para Residencial')
print('C para Comercial')
print('I para Industrial')
instalacao = input('Tipo de Instalacao: ')
preco = 0.0

if instalacao == 'R':
  preco = 0.65
  if consumo_kWh <= 500:
    preco = 0.40
  print(f'O preço a pagar é: R${consumo_kWh * preco:.2f}')

elif instalacao == 'C':
  preco = 0.60
  if consumo_kWh <= 1000:
    preco = 0.55
  print(f'O preço a pagar é: R${consumo_kWh * preco:.2f}')
  
elif instalacao == 'I':
  preco = 0.60
  if consumo_kWh <= 5000:
    preco = 0.55
  print(f'O preço a pagar é: R${consumo_kWh * preco:.2f}')

else:
  print('Tipo de instalação invalida')
