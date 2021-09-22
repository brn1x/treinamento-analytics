def valida_lista(string, lista):
  for el in lista:
    if el == string:
      return True
  return False

lista = ['python', 'javascript', 'java', 'c#', 'ruby', 'elixir']

print(valida_lista('Haskell', lista))
print(valida_lista('python', lista))
print(valida_lista('java', lista))