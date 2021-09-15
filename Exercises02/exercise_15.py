tabuada = int(input('Tabuada de : '))
inicio = int(input('Digite o inicio da tabuada: '))
fim = int(input('Digite o fim da tabuada: '))

while inicio <= fim:
  num = inicio * tabuada
  print(f'{inicio} X {tabuada} = {num}')
  inicio += 1