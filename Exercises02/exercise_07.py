valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos_a_pagar = int(input('Quantos anos demorará para a casa ser paga: '))

meses_a_pagar = anos_a_pagar * 12

preco_parcelas = valor_casa / meses_a_pagar

salario30percent = salario * 0.30

if preco_parcelas <= salario30percent:
  print(f'Sua casa pode ser comprada sendo paga em {meses_a_pagar} meses sendo R${preco_parcelas:.2f} mensal')
else:
  print(f'Seu salário não permite pagar uma casa desse preço')
