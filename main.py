from random import randint
class Student:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.progress = 0
    self.money = 100
    self.alive =True
  def study(self):
    self.progress += 20
    self.gladness -= 10
    print('Study time')
  def sleep(self):
    self.gladness += 35
    print('Sleep time')
  def chill(self):
    self.gladness += 15
    self.progress += 5
    self.money -=45
    print('Chill time')
  def work(self):
    self.money += 150
    self.gladness -=15
    print('Work time')
  def live():
    live_cube = randint(1,4)
    if live_cube == 1:
      self.study()
    elif live_cube == 2:
      self.sleep()
    elif live_cube == 3:
      self.chill()
    elif live_cube == 4:
      self.work()
  def final(self):
    if self.progress == 150:
      print('Amazing you pass')
    elif self.progress < -20:
      print('Too bed you dont pass')
    elif self.gladness < -20:
      print('Depression')
      self.alive = False
    elif self.money < -100:
      print('You have debts')
      self.alive = False

obj1 = Student('Bob')
for i in range(365):
  if obj1.alive == False:
    break
  obj1.live()
    
    
    
  