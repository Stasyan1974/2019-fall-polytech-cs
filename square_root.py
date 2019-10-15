def sqr(x, n):
  low = 0
  high = 2x - low
  while low <= high:
      m = (low + high) / 2
      t = m**2 - x
      if abs(t) < n:
          return round(m, 4)
      elif t < 0:
          low = m + n
      else:
          high = m - n
  return "x < 0"
