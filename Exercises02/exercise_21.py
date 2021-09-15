divida = float(input('Digite a quantidade da divida: '))
taxa = float(input('Digite o juro mensal: '))
pagamento_mensal = float(input('Digite o pagamento mensal da dívida: '))

taxa = taxa / 100

if (divida * taxa >= pagamento_mensal):
  print('Sua divida nunca será paga')
else:
  pago = 0.0
  meses = 1
  juros_pago = 0
  while (pago <= divida):
    juros = divida * taxa
    juros_pago += juros
    divida += juros
    pago += pagamento_mensal
    print(f'Mes {meses} | Divida: {divida:.2f} | Pago: {pago:.2f}')
    meses += 1

  print(f'Irá demorar {meses} para pagar e foi pago R${juros_pago:.2f} de juros')