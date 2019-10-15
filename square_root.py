def sqr(x):
  y = [i for i in range(0, 1001)]
  low = 0
  high = len(y)-1
  while low <= high:
      m = (low + high) // 2
      if y[m]**2 == x:
          return y[m]
      elif y[m]**2 < x:
          low = m + 1
      else:
          high = m - 1
  return "x < 0 или корень из х не целое число или корень из х больше 1000"
      
