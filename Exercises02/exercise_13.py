fim = int(input('Digite o número para finalizar: '))

num = 1
contador = 1

while num <= fim:
  if num % 3 == 0 and contador <= 10:
    contador += 1
    print(num)
  num += 1