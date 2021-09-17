l1 = [0,0,0]
l2 = [0,0,0]

x = 0
for i in l1:
  l1[x] = int(input(f'Digite o {i+1}º numero da lista 1: '))
  x += 1

x = 0
for i in l2:
  l2[x] = int(input(f'Digite o {i+1}º numero da lista 2: '))
  x += 1

l3 = []
l3.extend(l1)
l3.extend(l2)
print(l3)