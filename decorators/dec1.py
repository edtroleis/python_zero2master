# decorator
def my_decorator(func):
  def wrap_function():
    print('**********')
    func()
    print('**********')
  return wrap_function

@my_decorator
def hello():
  print('Hello World')

@my_decorator
def bye():
  print('Bye World')
  
hello()
bye()