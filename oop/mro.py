# mro - method resolution order
class A:
  print('class A')
  num = 10
  
class B(A):
  print('class B')

class C(A):
  print('class C')

class D(B, C):
  print('class D')

print(D.num)
print(D.__mro__)

#     A
#   /   \
# /       \
# B        C
# \       /
#   \   /
#     D