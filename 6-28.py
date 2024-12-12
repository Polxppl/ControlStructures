a = 0
b = 1
print(a)
print(b)
for i in range(0, 19):
  curr = a + b
  a = b
  b = curr
  print(curr)
