distancia_km = float(input('Digite a distancia a ser percorrido em KM: '))

if distancia_km <= 200:
  print(f'Distancia percorrida foi {distancia_km} e será cobrado R$ 0.50 por KM ficando o total de R$ {distancia_km * 0.50}')
else:
  print(f'Distancia percorrida foi {distancia_km} e será cobrado R$ 0.45 por KM ficando o total de R$ {distancia_km * 0.45}')