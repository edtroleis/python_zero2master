# map, filter, zip and reduce

my_list = [1, 2, 3]
your_list = [4, 5, 6]
other_list = [7, 8, 9]

def multiply_by2(item):
  return item * 2

def only_odd(item):
  return item % 2 != 0

print(list(zip(my_list, your_list, other_list)))
print(my_list)
