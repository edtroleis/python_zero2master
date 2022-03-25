class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def run(self):
    print('run')
    return 'done'
    
player1 = PlayerCharacter('troleis', 38)
print(player1.name)
print(player1.age)