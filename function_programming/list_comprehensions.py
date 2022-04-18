# list, set and dictnary comprehensions

my_list_comprehention = [char for char in 'hello']
print(my_list_comprehention)

my_list = []
for char in 'hello':
  my_list.append(char)

print(my_list)


my_list2_comprehention = [num for num in range(0, 10)]
print(my_list2_comprehention)

my_list2 = []
for num in range(0, 10):
  my_list2.append(num)
print(my_list2)


my_list3_comprehention = [num**2 for num in range(0, 10) if num % 2 == 0]
print(my_list3_comprehention)
