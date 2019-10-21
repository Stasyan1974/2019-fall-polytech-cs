def quicksort(array):
  if len(array) < 2:
    return array
  else:
    mid = array[0]
    left = [i for i in array[1:] if i <= mid]
    right = [i for i in array[1:] if i > mid]
    return quicksort(left) + [mid] + quicksort(right)
