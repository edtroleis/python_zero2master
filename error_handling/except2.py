
while True:
  try:
    age = int(input('what is your age? '))
    10 / age
    break
  except ValueError:
    print('please enter a number')
  except ZeroDivisionError:
    print('please enter a number other than zero')

