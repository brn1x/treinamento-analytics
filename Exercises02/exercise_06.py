num_a = int(input('Digite o primeiro número: '))
num_b = int(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada (* - / +): ')

valorFinal = 0

if (operacao == '+'):
  valorFinal = num_a + num_b
elif (operacao == '-'):
  valorFinal = num_a - num_b
elif (operacao == '*'):
  valorFinal = num_a * num_b
elif (operacao == '/'):
  valorFinal = num_a / num_b
elif (operacao == '//'):
  valorFinal = num_a // num_b
else:
  print('Operação inválida')

if (valorFinal != 0):
  print(f'O valor da operação {num_a} {operacao} {num_b} é igual a {valorFinal}')