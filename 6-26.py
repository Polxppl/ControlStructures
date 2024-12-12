attempts = 0
pin = '1234'
user_input = ''
while attempts < 3 and pin != user_input:
  user_input = input('Enter the PIN code: ')
  attempts += 1
  if user_input != pin:
    print('Incorrect...')

if user_input == pin:
  print('PIN is correct')
else:
  print('Sorry, your payment card has been blocked.')


