def lus(s):
  i = 1
  uniq = 1
  res = 1
  end = len(s) - 1
  while i <= end:
    if s[i] != s[i-1]:
      uniq += 1
    else:
      uniq = 1
    if res < uniq:
      res = uniq
    i += 1
  return res
  
def test_lus(s, res, testId):
  if lus(s) == res:
    print("Test " + str(testId) + " complete")
    
 # ТЕСТ
 s1 = "abcdeeeeefghhhhhijklmnop"
 test_lus(s1, 9, 1))
 
 s2 = "1234567890"
 test_lus(s2, 10, 2)
