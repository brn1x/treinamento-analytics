string = '012345678901234567890123456789012345678901234567890123456789'
n = 10

r = [string[i:i+n] for i in range(0, len(string), n)]
r = '.'.join(r)
print(r)

print('\n -----------------------------------------------------------\n')

lista = []
for i in range(0, len(string), n):
  lista.append(string[i:i+n])

print('.'.join(lista))