# set and dict comprehensions

# set
my_list = {char for char in 'hello'}
print(my_list)


# dict
simple_dict = {'a': 1, 'b': 2, 'c': 3}

# dict comprehension
my_dict_comprehention = {key: value**2 for key, value in simple_dict.items()}
# my_dict_comprehention = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict_comprehention)

# normal dict
my_dict = {}
for key, value in simple_dict.items():
  my_dict[key] = value**2
print(my_dict)

# other example
my_dict2_comprehention = {num:num*2 for num in [1,2,3,4]}
print(my_dict2_comprehention)