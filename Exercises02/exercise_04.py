salario = float(input('Digite seu salário: '))

if salario >= 1250:
  print(f'Você recebeu um aumento, seu salário agora é {salario * 1.10}')
else:
  print(f'Você recebeu um aumento, seu salário agora é {salario * 1.15}')