# project_code_s
class Base1(object):
    def _init_(self):
        self.str1="Geek1"
        print ("Base1")


class Base2(object):
    def _init_(self):
        self.str2="Geek2"
        print ("Base2")

class Derived(Base1,Base2):
    def _init_(self):
        Base1._init_(self)
        Base2._init_(self)
        print("Derived")
    def printStrs(self):
        print(self.str1,self.str2)
ob = Derived()
ob.printStrs()
