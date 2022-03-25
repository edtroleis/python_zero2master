class PlayerCharacter:
  def __init__(self, name, age):  # dunder method
    self._name = name             # _name means private variable
    self._age = age               # _age means private variable
    
  def run(self):
    print('run')
    
  def speak(self):
    print(f'my name is {self._name}, and I am {self._age} years old')
    
player1 = PlayerCharacter('troleis', 38)
print(player1.speak())