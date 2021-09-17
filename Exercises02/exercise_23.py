preco_a_pagar = 0

while True:
  codigo_produto = int(input('Digite o código do produto ou 0 para sair: '))
  preco = 0
  if codigo_produto == 0:
    break

  elif codigo_produto == 1:
    preco = 0.50

  elif codigo_produto == 2:
    preco = 1.00

  elif codigo_produto == 3:
    preco = 4.00

  elif codigo_produto == 5:
    preco = 7.00

  elif codigo_produto == 9:
    preco = 8.00

  else:
    print('Codigo invalido')

  if preco != 0:
    quantidade = int(input('Quantidade do produto: '))
    preco_a_pagar = preco_a_pagar + (preco * quantidade)

print(f'Total a pagar R${preco_a_pagar:.2f}')