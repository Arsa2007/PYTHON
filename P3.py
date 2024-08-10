class Students:

  def __init__(self, name, physics, chemistry, maths):
    self.name = name
    self.physics = physics
    self.chemistry = chemistry
    self.maths = maths

  def average(self):
    print(self.name)
    a = (self.physics + self.chemistry + self.maths) / 2
    print(a)


a, b, c, d = input(), int(input()), int(input()), int(input())
S1 = Students(a, b, c, d)
S1.average()
print(S1)
