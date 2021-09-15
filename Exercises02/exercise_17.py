# Fazer divisão sem utilizar divisão

num_01 = int(input('Digite o primeiro número: '))
num_02 = int(input('Digite o segundo número: '))

resultado = num_01
contador = 0

while resultado > 0 :
  resultado = resultado - num_02
  contador += 1

print(f'{num_01} / {num_02} = {contador}')
