l1 = [1, 2, 3, 4, 5]
ex1 = [var for var in l1]
print(ex1)
print('\n-')

ex2 = [v * 2 for v in l1]
print(ex2)
print('\n-')

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)
print('\n-')

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)
print('\n-')

tupla = (
  ('chave', 'valor'),
  ('chave2', 'valor2')
)

ex5 = [(y, x) for x,y in tupla]
ex5 = dict(ex5)
print(ex5)
print('\n-')

l3 = list(range(100))

ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)
print('\n-')

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)


