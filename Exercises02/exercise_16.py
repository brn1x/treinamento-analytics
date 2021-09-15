num_01 = int(input('Digite o primeiro número: '))
num_02 = int(input('Digite o segundo número: '))

resultado = 0
while (num_02 > 0):
  resultado += num_01
  num_02 -= 1

print(resultado)