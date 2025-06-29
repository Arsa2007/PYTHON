from abc import ABC,abstractmethod
class Department(ABC):
    @abstractmethod
    def courselist():
        pass


class Course(Department):
    def courselist(self,course1=0,course2=0,course3=0):
     course1=""
     course2=""
     course3=""
class Person():
 def __init__(self,name,age):
     self.name=name
     self.age=age
 def displayprofile():
     pass    


class Student(Person,Course):
    def __init__(self,name,age,rollno,course1,course2=0,course3=0):
      self.name=name
      self.age=age  
      self.rollno=rollno
      self.course1=course1 
      self.course2=course2
      self.course3=course3
      super().courselist(course1,course2,course3)
      super().__init__(name,age)    
    def displayprofile(self):
       print(self.name)
       print(self.age)
class Teacher(Person):
    def __init__(self,name,age,employeeID, subject):
       self.name=name
       self.age=age        
       self.emmployeeID=employeeID
       self.subject=subject 
       super().__init__(name, age) 
    def displayprofile(self):
       print(self.name)
       print(self.age)
class Result(Student):
    def __init__(self,marks,grade):
        self._marks=marks
        self._grade=grade
    def generateReport(self,marks,grade):
        a=self._marks=marks
        b=self._grade=grade
        print(a,b)
        
                   

       
o1=Student('abc',15,18,'Science')
o1.courselist('science','maths','maths-2')   
o1.displayprofile()          

             
     