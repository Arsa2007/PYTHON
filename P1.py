from abc import ABC,abstractmethod
class LibraryDepartment(ABC):
    @abstractmethod
    def managesection():
        pass
    
    @abstractmethod
    def Sciencesection():
        pass
    
    @abstractmethod    
    def Artssections():
        pass 





class Member():

 def __init__(self,memberID,name,contact):
     self.memberID=memberID
     self.name=name
     self.contact=contact
 def caculatefine(self,days,collegename):
     if collegename is None:
         a=10
         return days*a
     else:
         b=20
         return days*b



class Studentmember(Member):
    def __init__(self,collegename,memberID,name,contact):
        self.collegename=collegename 
        super().__init__(memberID,name,contact) 
        super().caculatefine(days=0,collegename=None)
        
class Facultymember(Member):
    def __init__(self,department,memberID,name,contact):
        self.department=department
        super().__init__(memberID,name,contact) 
        super().caculatefine(days=0,collegename=None)
        
        
class Transaction(Member):
    def __init__(self,bookID,issueDate,returnDate):
        self.__bookID=bookID
        self.__issueDAte=issueDate
        self.__returnDate=returnDate
        
               
student = Studentmember(1,"Alice","1234567890","ABC College")
print(student.caculatefine(3,'ABC College'))


               
