ultimo = 4
fila = list(range(1, ultimo + 1))
ultimo2 = 4
fila2 = list(range(1, ultimo + 1))

while True:
  print(f'Existem {len(fila)} clientes na fila!')
  print(f'Fila - 1 atual: {fila}')
  print(f'Fila - 2 atual: {fila2}')
  print(f'F para adicionar um cliente ao fim da fila 1')
  print(f'A para realizar o atendimento da fila 1')
  print(f'G para adicionar um cliente ao fim da fila 2')
  print(f'B para realizar o atendimento da fila 2')

  print(f'S para sair')

  op = input('Operação A, B, F, G ou S: ')

  if op.upper() == 'A':
    if(len(fila)) > 0:
      atendido = fila.pop(0)
      print(f'Cliente {atendido}')
    else:
      print(f'Fila vazia! Ninguem para atender')
  elif op.upper() == 'B':
    if(len(fila2)) > 0:
      atendido = fila2.pop(0)
      print(f'Cliente {atendido}')
    else:
      print(f'Fila vazia! Ninguem para atender')
  elif op.upper() == 'F':
    ultimo += 1
    fila.append(ultimo)
  elif op.upper() == 'G':
    ultimo2 += 1
    fila2.append(ultimo2)
  elif op.upper() == 'S':
    break
  else:
    print(f'Operação inválida! Digite apenas F, A ou S')

  print('\n')
