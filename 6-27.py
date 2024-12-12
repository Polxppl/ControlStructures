row = 2

while row >= 0:
  column = 0
  while column < 3:
    print(row * 3 + 1 + column, end=' ')
    column += 1
  row -= 1
  print()
