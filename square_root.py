def sqr(x):
  low = 0
  high = 1000
  while low <= high:
      m = (low + high) / 2
      if round(m**2, 2) == x:
          return round(m, 2)
      elif round(m**2, 2) < x:
          low = m + 0.001
      else:
          high = m - 0.001
  return "x < 0 или корень из х больше 1000"
