from abc import ABC,abstractmethod
class Department(ABC):
  @abstractmethod
  def onCallStatus():
    pass  

  @abstractmethod
  def  displayinfo():  
   pass


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayinfo():
        print(self.name) 
        print(self.age)  
    def onCallStatus():
     pass  
     

class Patient(Person):
  def __init__(self,name,age,disease):
    self.disease = disease
    Person.__init__(self,name,age)
  def displayinfo():
        print(self.name) 
        print(self.age)  
    
  def onCallStatus():
    pass
class Doctor(Person):
  def __init__(self,name1,age,degree):
    self.name1=name1
    self.degree = degree
    Person.__init__(self,name,age)  
  def displayinfo():
        print(self.name) 
        print(self.age)  
class Surgeon(Doctor):
  
  def __init__(self,name,age,disease,sepecialization):
    self.name=name
    self.age=age
    self.disease=disease
    self.sepecialization=sepecialization
    Person.__init__(self,name,age)  

  def onCallStatus():
    pass
  def displayinfo():
    pass  

class Staff(Person):
  role='Helping'
  def __init__(self,name,age,disease):
    self.name=name
    self.age=age
    self.disease=disease
    def onCallStatus():
      pass
    def displayinfo():
      pass    

class Time(Person,Doctor):
  def __init__(self,name,age,disease,time):  
      Person.__init__(self,name,age) 
      self._patientName=Person.name
      self._doctorName=Doctor.name
      self.__appointmentTime=time
  def onCallStatus():
      pass
  def displayinfo():
      pass       

