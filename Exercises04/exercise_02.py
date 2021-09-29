def add (todo, todo_list):
  todo_list.append(todo)

def list (todo_list):
  for idx,todo in enumerate(todo_list):
    print(f'{idx + 1} - {todo}')
  print('\n')

def undo (todo_list, redo_list):
  add(todo_list.pop(), redo_list)

def redo (todo_list, redo_list):
  add(redo_list[len(redo_list) - 1], todo_list)
  redo_list.pop()

def main():
  todo_list = []
  redo_list = []
  add('teste 1', todo_list)
  add('teste 2', todo_list)
  add('teste 3', todo_list)
  add('teste 4', todo_list)
  list(todo_list)

  undo(todo_list, redo_list)
  undo(todo_list, redo_list)
  undo(todo_list, redo_list)
  list(todo_list)

  redo(todo_list, redo_list)
  redo(todo_list, redo_list)
  redo(todo_list, redo_list)
  list(todo_list)

if __name__ == '__main__':
  main()
