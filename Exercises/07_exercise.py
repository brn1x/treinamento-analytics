name = 'Bruno'
age = 23
height = 1.75
weight = 67.5
actual_year = 2021

def get_person_birth_year(age, actual_year):
  return actual_year - age

def get_person_IMC(weight, height):
  return weight / height **2

def get_person_info():
  return f'Hello my name is {name}, I\'m {age} years old, actually I\'m {height} tall, i weigh {weight} KG and I was born in {get_person_birth_year(age, actual_year)}'

print(get_person_info())
print(f'IMC: {get_person_IMC(weight, height):.2f}')
