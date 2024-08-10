class StdAcc:
  def __init__(self,name,account_no,balance):
    self.name=name
    self.account_no=account_no
    self.balance=balance

  def credit(self,amount):
      self.balance= amount +self.balance
      print(self.balance)

  def debit(self,amount):
      self.balance= self.balance -amount
      print(self.balance)



s=StdAcc("Ram",123,1000)
print(s)
s.credit(100)
s.debit(500)