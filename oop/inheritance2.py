class User():
  def sign_in(self):
    print('logged in')
    
class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows
    
wizard1 = Wizard('troleis', 38)
print(isinstance(wizard1, User))