def pesquise(lista, valor):
  if valor in lista:
    indice = lista.index(valor)
    return lista[indice]

l = [1,2,3,4]
print(pesquise(l, 3))
print(pesquise(l, 5))
