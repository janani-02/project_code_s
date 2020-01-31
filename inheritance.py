

class human:
    species="h.sapiens"
def _init_(self,name):
    self.name=name
    self.age=0
def say(self,msg):
    print("{name}:{message}".format(name=self.name,message=msg))
def sing(self):
    return'yo...yo..microphone check...onetwo'
def get_species(cls):
    return cls.species
def grunt():
    return "**grunt**"

class person(object):
    def _init_(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(person):
    def _init_(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person._init_(self,name,idnumber)
a=person('rahul',88602)
print(a)

class A:
    def _init_(self,n='rahul'):
        self.name=n
class B(A):
    def _init_(self,roll):
        self.roll=roll
object=B(23)
print(pbject.name)
