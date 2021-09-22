from turtle import Turtle
t = Turtle()
print(t)

direcao_turtle = 'direita'
t.speed(1)

while True:
  print('F -> Frente')
  print('T -> Trás')
  direcao = input('Andar para frente ou para trás?: ')
  if (direcao.lower() == 't'):
    t.left(180)
  elif (direcao.lower() == 'f'):
    t.right(180)

  pixels = int(input('\nQuantos pixels a serem percorridos: '))

  t.forward(pixels)
  pixels = 0
  print('\nS -> SIM')
  print('N -> NÃO')
  continuar = input('\nDeseja continuar?: ')
  if (continuar.lower() == 'n'):
    break

print('Obrigado!')
