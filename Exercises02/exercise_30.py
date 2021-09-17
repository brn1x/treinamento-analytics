l = [15, 7, 27, 39]

p = int(input('Digite o valor a ser pesquisado: '))
x = 0

while x < len(l):
  if l[x] == p:
    print(f'{p} achado na posição {x}')
    break
  elif x == len(l) - 1:
    print(f'{p} não encontrado')
  x += 1