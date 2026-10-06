'''
Inheritance:
-----------
--> Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance, Hybrid Inheritance

'''
#banking example -->single inheritance
class RBI:
    """Base Class"""
    cash=10000000 #class variable
    #class method
    @classmethod
    def available_cash(cls):
        print(f"Available cash in RBI is {cls.cash}")
'''
u1=RBI()
u1.available_cash() #accessing class method using object
print(u1.cash)
RBI.available_cash()'''

class SBI(RBI):
    """Derived Class"""
    
'''
u1=SBI()
print(u1.cash)
u1.available_cash() #accessing class method from base class using derived class
SBI.available_cash() #accessing class method from base class using derived class

class HDFC(RBI):
    """Derived Class-2"""
    cash=5000000 #class variable
    @classmethod
    def hdfc_cash(cls):
        print(f"Available cash in HDFC is {cls.cash}")
        print(f'total cash in RBI and HDFC is {cls.cash+RBI.cash}')

u1=HDFC()
u1.hdfc_cash() #accessing class method from derived class
u1.available_cash() #accessing class method from base class using derived class
print(u1.cash)#here class variable cash is overridden in derived class HDFC, so it will print 5000000

#task: convert same intohierarchical also make use of public,private along with class methods and class variables
#kid-father Property Scenario -->Constructor overriding,method overriding

class Father:
    """Father Property only in cash"""
    def __init__(self):
        self.f_property=500000
    def father_prop(self):
        print(f'Father Property is {self.f_property}')



class Kid(Father):
    """Kid started earning and saved some amount"""
    def __init__(self):
        self.property=250000 #here child class constructor will over ride the parent class constructor when having same name
    def kid_property(self):
        print(f'Kids property is {self.property}')
        print(f"Total property is {self.property+self.f_property}")# here we will get attribute error because

dad=Father()
dad.father_prop()
obj=Kid()
obj.father_prop()
obj.kid_property()

#above we seen constructor overriding means if parent class const and father

#Constructor overloading can be avoided using super keyword

class Father:
    """Father Property only in cash"""
    def __init__(self):
        self.f_property=500000
    def father_prop(self):
        print(f'Father Property is {self.f_property}')



class Kid(Father):
    """Kid started earning and saved some amount"""
    def __init__(self):
        super().__init__()# here we will call super/parent class'es constructor so we get f_property
        self.property=250000 #here child class constructor will over ride the parent class constructor when having same name
    def kid_property(self):
        print(f'Kids property is {self.property}')
        print(f"Total property is {self.property+self.f_property}")# here we will get attribute error because

dad=Father()
dad.father_prop()
obj=Kid()
obj.father_prop()
obj.kid_property()

#class superclass constructor with args
class Father:
    """Father Property only in cash"""
    def __init__(self,prop1):
        self.f_property=prop1
    def father_prop(self):
        print(f'Father Property is {self.f_property}')



class Kid(Father):
    """Kid started earning and saved some amount"""
    def __init__(self,prop1,prop2):
        super().__init__(prop1)
        self.property=prop2 
    def kid_property(self):
        print(f'Kids property is {self.property}')
        print(f"Total property is {self.property+self.f_property}")# here we will get attribute error because

u1=Kid(500000000,2000000)
u1.father_prop()
u1.kid_property()

#method overriding -->When we define same method name in parent class and also in child class, it will result in method overriding
# just like how it happend with constructor super().method()

class Square:
    def __init__(self,x):
        self.x=x
    def area(self):
        return f'Area of Square is {self.x**2}'

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        print(super().area())
        return f'Area of Rectangle is {self.x*self.y}'

x,y=map(int,input("Enter values: ").split(' '))
r=Rectangle(x,y)
print(r.area())'''

#Multiple Inheritance: one derivied clas swith more than one base classes
#parent(Father,Mother)-->child 

