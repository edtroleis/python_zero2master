class PlayerCharacter:
  
  membership = True
  
  def __init__(self, name, age):
    if (PlayerCharacter.membership):
      self.name = name
      self.age = age
  
  def shout(self):
    print(f'my name is {self.name}')
  
  def run(self, age):
    print(f'my age is {self.age}')
  
player1 = PlayerCharacter('troleis', 38)

print(player1.name)
print(player1.shout())
print(player1.run(38))
