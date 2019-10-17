def find_smallest(arg):
  smallest = arg[0]
  smallest_index = 0
  for i in range(1, len(arg)):
    if arg[i] < arg[0]:
      smallest = arg[i]
      smallest_index = i
  return smallest_index

def selection_sort(arg):
  list = []
  for i in range(len(list)):
    smallest_index = find_smallest(arg)
    list.append(arg[smallest_index])
  return list
