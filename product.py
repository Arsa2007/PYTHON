from abc import ABC,abstractmethod
class Warehouse(ABC):
    @abstractmethod
    def TrackInventory():
        pass
class LocalWarehouse(Warehouse):
    def TrackInventory():
        pass
    
    
class CentralWarehouse(Warehouse):
    def TrackInventory():
        pass    
    
    
class Product():
    def __init__(self,productID,name,price,warranty=None,material=None):
        self.productID=productID
        self.name=name  
        self.price=price
        self.warranty=warranty 
        self.material=material 
class Electronics(Product):
    def __init__(self, productID, name, price,warranty,material):
        self.warranty=warranty
        self.material=material
        super().__init__(productID, name, price,warranty,material)
    def getdetails(self,productID, name, price,warranty,material):
        super().__init__(productID, name, price,warranty,material)    


class Furtniture(Product):
    def __init__(self,productID, name, price,warranty,material):
        self.material=material 
        self.warranty=warranty
        super().__init__(productID,name,price,warranty=None,material=None) 
    def getdetails(self,productID, name, price,warranty,material):
        super().__init__(productID, name, price,warranty,material)    
 
class Order(Product):
   def __init__(self,placement,quantity,date):
    self.placement=placement
    self.qunatity=quantity
    self.date=date
        
   def getOrder(self,productID,order,name,price,warranty,material):

        self.order=order  
        if order=='electronics':
          super().__init__(productID,name,price,warranty,material)
        else:
          super().__init__(productID,name,price,warranty=None,material=None)   
class Supplier(Electronics,Furtniture):
   def __init__(self, productID, name, price, warranty, material):
        
    ItemType=input("Enter the type of Item ")  
    if ItemType=="Electronics":
        supplier="XYZ"
        super().__init__(productID, name, price,warranty,material)
    else:
        supplier="ABC"
        super().__init__(productID, name, price,warranty,material)            
o1=Product(23,1,23,3,4) 
         
print(o1.name)