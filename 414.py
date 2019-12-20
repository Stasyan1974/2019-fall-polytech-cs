def MaxSubstring(s):
  i = 1
  counter = 1
  res = 1
  end = len(s) - 1
  while i <= end:
    if s[i] != s[i-1]:
      counter += 1
    else:
      counter = 1
    if res < counter:
      res = counter
    i += 1
  return res
    
 # ТЕСТ
if __name__ == __main__: 
  assert (MaxSubstring("abcdddddertffffxxxotfewqvn") == 9), "программа работает неправильно"
  assert (MaxSubstring("12345678999abcc") != 9), "программа работает правильно"
