def mdc(num1, num2, iterator = 1, maior = 0):
  if num1 >= iterator and num2 >= iterator:
    if (num1 % iterator) == 0 and (num2 % iterator) == 0:
      maior = iterator
    iterator += 1
    return mdc(num1, num2, iterator, maior)
  return maior

print(mdc(6,18))