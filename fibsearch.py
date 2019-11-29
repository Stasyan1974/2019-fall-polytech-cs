# arr - список, x - искомый аргумент списка.
def fibsearch(arr, x):
  n = len(arr)
  fib2 = 0 # Число Фибоначчи, находящееся на две позиции ниже, чем fib
  fib1 = 1 # Число Фибоначчи, находящееся на одну позицию ниже, чем fib
  fib = fib1 + fib2
  # Присвоим переменной fib такое значение, чтобы оно было таким МИНИМАЛЬНЫМ числом, которое БОЛЬШЕ ИЛИ РАВНО n
  while fib < n:
    fib2 = fib1
    fib1 = fib
    fib = fib1 + fib2
  # Введём переменную смещения
  offset = -1
  while fib > 1:
    i = min(offset + fib2, n - 1)
    if arr[i] < x:
      fib = fib1
      fib1 = fib2
      fib2 = fib - fib1
      offset = i
    elif arr[i] > x:
      fib = fib2
      fib1 = fib1 - fib2
      fib2 = fib - fib1
    else:
      return i
  if fib1 and arr[offset+1] == x:
    return offset + 1
  return -1
