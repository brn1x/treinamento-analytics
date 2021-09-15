tabuada = int(input('Tabuada de : '))

num = 1
iterador = 1

while iterador < tabuada:
  num = iterador * tabuada
  print(f'{iterador} X {tabuada} = {num}')
  iterador += 1