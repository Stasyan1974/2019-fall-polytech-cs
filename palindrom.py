def pal(x):
  x = x.lower()
  return x == "".join(reversed(x)):

# Тест
if __name__ == __main__:       # ?
  assert pal("LEveL") == True
  assert pal("IFNIT") == False
