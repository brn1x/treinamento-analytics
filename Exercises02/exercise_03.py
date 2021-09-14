num_a = int(input('Digite o primeiro número: '))
num_b = int(input('Digite o segundo número: '))
num_c = int(input('Digite o terceiro número: '))

maior = num_a

if num_b > num_a and num_b > num_c:
  maior = num_b
elif num_c > num_a and num_c > num_b:
  maior = num_c

menor = num_a

if num_b < num_a and num_b < num_c:
  menor = num_b
elif num_c < num_a and num_c < num_b:
  menor = num_c

print(f'O menor número é o {menor} e o maior é {maior}')