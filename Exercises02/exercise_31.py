compras = []
while True:
  produto = input('Produto: ')
  if produto == 'fim':
    break
  quantidade = int(input('Quantidade: '))
  preco = float(input('Preco: '))
  compras.append([produto, quantidade, preco])

soma = 0.0

for e in compras:
  print(f'{e[0]} x {e[1]}, {e[2]:.2f} = {e[1] * e[2]:.2f}')
  soma += e[1] * e[2]

print(f'Total: {soma:.2f}')