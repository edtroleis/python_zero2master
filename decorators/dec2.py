# decorator

from time import time

def performance(fn):
  def wrapper(*args, **kw):
    t1 = time()
    result = fn(*args, **kw)
    t2 = time()
    print(f'took {t2-t1} ms')
    return result
  return wrapper
  
@performance
def long_time():
  for i in range(100000000):
    i*i
    
long_time()