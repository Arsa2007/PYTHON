class Area:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def rectangle(self):
        recarea=self.l+self.b
        print(recarea)
    def square(self):
        sqarea=(self.l)**2
        print(sqarea)


a=Area(2,3)
print(a)
a.rectangle()
a.square()
