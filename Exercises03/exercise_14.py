def generate_dict(string):
  dictionary = {}
  
  for char in string:
    if dictionary.get(char):
      dictionary[char] += 1
    else:
      dictionary[char] = 1
  return dictionary

input_str = input('Digite uma frase: ')
print(generate_dict(input_str))
