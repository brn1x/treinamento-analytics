estoque = {
  "tomate": [1000, 2.30],
  "alface": [500, 0.45],
  "batata": [2001, 1.20],
  "feijao": [100, 1.50]
}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]

total = 0

print("Vendas: \n")
for operacao in venda:
  produto, quantidade = operacao
  preco = estoque[produto][1]
  custo = preco * quantidade
  print(f'{produto}: {quantidade} - {preco} - {custo}')
  estoque[produto][0] -= quantidade
  total += custo
  print(f"Custo total {total:.2f}")
  print("Estoque: \n")
  for chave, dados in estoque.items():
    print("Descrição", chave)
    print("Quantidade", dados[0])
    print(f"Preço: {chave:.2f}")