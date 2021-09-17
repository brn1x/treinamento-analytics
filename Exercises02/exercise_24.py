valor = float(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100.00
a_pagar = valor

while True:
  a_pagar = float(format(a_pagar, ".2f"))

  if atual <= a_pagar:
    a_pagar -= atual
    cedulas += 1
  else:
    print(f'{cedulas:.0f} de R$ {atual:.2f}')
    if a_pagar == 0:
      break
    
    if atual == 100.00:
      atual = 50.00
    elif atual == 50.00:
      atual = 20.00
    elif atual == 20.00:
      atual = 10.00
    elif atual == 10.00:
      atual = 5.00
    elif atual == 5.00:
      atual = 1.00
    elif atual == 1.00:
      atual = 0.50
    elif atual == 0.50:
      atual = 0.25
    elif atual == 0.25:
      atual = 0.10
    elif atual == 0.10:
      atual = 0.05
    elif atual == 0.05:
      atual = 0.01
    
    cedulas = 0