ultimo = 4
fila = list(range(1, ultimo + 1))

while True:
  print(f'Existem {len(fila)} clientes na fila!')
  print(f'Fila - 1 atual: {fila}')
  print(f'F para adicionar um cliente ao fim da fila')
  print(f'A para realizar o atendimento da fila')
  print(f'S para sair')
  print('Digite as operações separadas por virgula')
  op = input('Operação A, F ou S: ')

  # operations = op.split(',')

  for ope in op:
    if ope.upper() == 'A':
      if(len(fila)) > 0:
        atendido = fila.pop(0)
        print(f'Cliente {atendido} atendido')
      else:
        print(f'Fila vazia! Ninguem para atender')
    elif ope.upper() == 'F':
      ultimo += 1
      fila.append(ultimo)
    elif ope.upper() == 'S':
      break
    else:
      print(f'Operação inválida! Digite apenas F, A ou S')

  print('\n')
