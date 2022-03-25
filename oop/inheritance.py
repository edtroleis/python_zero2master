class User():
  def sign_in(self):
    print('logged in')
    
class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power
    
  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows
    
  def attack(self):
    print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('troleis', 38)
archer1 = Archer('eduardo', 50)

wizard1.attack()
wizard1.sign_in()

archer1.attack()
archer1.sign_in()