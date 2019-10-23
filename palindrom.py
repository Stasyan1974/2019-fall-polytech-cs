def pal(data1):
  data1 = data1.lower()
  data2 = reversed(data1)
  for x, y in zip(data1, data2):
    if x == y:
      print("yes")
    else:
      print("no")
      
# Тест
if __name__ == __main__:       
  assert pal("AbbA") == "yes\nyes\nyes\nyes"
  assert pal("aReA") == "yes\nno\nno\nyes"
