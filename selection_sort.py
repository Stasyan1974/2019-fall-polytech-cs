def find_smallest(arg):
  smallest = arg[0]
  smallest_index = 0
  for i in range(1, len(arg)):
    if arg[i] < smallest:
      smallest = arg[i]
      smallest_index = i
  return smallest_index

def selection_sort(arg):
  sp = []
  for i in range(len(arg)):
    smallest_index = find_smallest(arg)
    sp.append(arg.pop(smallest_index)) # .pop удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
  return sp
