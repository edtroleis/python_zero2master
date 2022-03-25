class Cat:
  species = 'mammal'
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    

cat1 = Cat('bartho', 6)
cat2 = Cat('luna', 3)
cat3 = Cat('pingo', 1)


def oldest_cat(obj_list):
  oldest = obj_list[0].age
  for i in obj_list:
    if oldest < i.age:
      oldest = i.age
  return oldest

def oldestcat(*list):
  agecase = []
  for i in list:
    agecase.append(i.age)
  print(f'The oldest cat is {max(agecase)} years old.')

print(f'gato mais velho tem {oldest_cat([cat1, cat2, cat3])} anos')

oldestcat(cat1, cat2, cat3)