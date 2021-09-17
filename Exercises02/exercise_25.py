notas = [0]*7
soma = 0
x = 0

while x < len(notas):
  notas[x] = float(input(f'Nota {x + 1}: '))
  soma += notas[x]
  x += 1

x = 0

while x < len(notas):
  print(f'Nota {x}: {notas[x]:.2f}')
  x += 1

print(f'Media: {soma/x:.2f}')
