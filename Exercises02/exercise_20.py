deposito = float(input('Digite o deposito: '))
deposito_mensal = float(input('Digite o aporte mensal: '))
taxa = float(input('Digite a taxa anual: '))

taxa = (taxa / 12) / 100

contador = 1
resultado = deposito

while (contador <= 24):
  resultado = resultado + deposito_mensal
  rendimento = (resultado + deposito_mensal) * taxa
  resultado = resultado + rendimento
  print(f'Mes - {contador} | Redimento: R${rendimento:.2f} - Total Depositado: R${resultado:.2f}')
  contador += 1
