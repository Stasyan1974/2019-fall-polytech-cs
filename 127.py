def fact(num):
  sieve = [True] * (num + 1)
  index = 2
  fact_decomp = str(num) + "! = 1"
  fact_num = 1
  while index <= num:
    if sieve[index] == True:
      # Подсчёт степени
      degree = 0
      div = index
      while div <= num:
        degree += num // div
        div *= index
      fact_decomp += " * " + str(index) + "^" + str(degree)
      fact_num *= index ** degree
      # Убираем лишнее (Решето Эратосфена)
      mult = index * index
      while mult <= num:
        sieve[mult] = False
        mult += index
    index += 1
  return(fact_decomp, fact_num)
  
