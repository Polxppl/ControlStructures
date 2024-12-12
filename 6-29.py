number = int(input('Enter number: '))

factors_found = False

for i in range(2, int(number / 2) + 1):
  if number % i == 0:
    factors_found = True
    break

if factors_found:
  print('Not a prime')
else:
  print('Prime')
