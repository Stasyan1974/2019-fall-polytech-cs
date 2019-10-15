def sqr(num, n):
  low = 0
  high = num
  while low <= high:
      m = (low + high) / 2
      t = m**2 - num
      if abs(t) < n:
          return round(m, 4)
      elif t < 0:
          low = m
      else:
          high = m
  return "num < 0"
