def nod(x, y): 
  while x != 0 and y != 0:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x + y # нахождение НОД(x, y) по алгоритму Евклида

def nok(x, y):
  return x * y / nod(x, y) # нахождение НОК(x, y) через связь с НОД(x, y)
  
def nok3(l, m, k):
  return nok(nok(l, m), k) # НОК трёх периодов и есть частота выстраивания планет в одну линию

# Тест
if __name__ == __main__:
  assert nok3(2, 5, 15) == 30.0
  assert nok3(3, 6, 13) == 78.0
