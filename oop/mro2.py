class X:
  print("class X")
  
class Y:
  print("class Y")
  
class Z:
  print("class Z")
  
class A(X, Y):
  print("class A")
  
class B(Y, Z):
  print("class B")
  
class M(B, A, Z):
  print("class M")
  
print(M.__mro__)
