def fibonacci(n):
  contador = 0
  total = [1]
  while n >= 1:
    total.append(total[contador - 1] + total[contador])
    n -= 1
    contador += 1
  return total

print(fibonacci(11))
