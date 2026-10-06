'''
oop --> Object Oriented Programming ---> It is a principle or paradigm which revolves around the concept of objects. It is a programming paradigm that uses objects and their interactions to design applications and computer programs.
to work with objects not only with functions.

It has two main concepts or object contains:
--->Atributes (data members) ---> Properties or Characteristics of an object
--->Methods (behaviors) ---> It performs some action for the object

An Object is a real world entity , where as a class is a blueprint of an object
chair -->object
Tools,Wood--> memory
Dimensions(Blueprint) --> class
Carpenter -->User

Syntax --> Class is the keyword to create a class

class ClassName:
    """docstring"""
    #Attributes (characteristics)
    .............
    #Methods (behaviors)
    def method(self):
        ............
        statements
        .............


a=ClassName()  #object creation
b=ClassName()  #object creation


class ClassName:
    """doc string"""
    def __init__(self,attrs):
        .............
        .............
'''
'''
#OOP --> Encapsulation,Inheritance,Polymorphism,Abstraction
#Encapsulation --> It is one of the key properties of OOP, which bundles the data including attributes and methods into a single class.
It provides accessibility (Public,Private,Protected)


#Students Class with basic details
class Students:
    """Students class with basic details"""
    #Attributes
    name="Akash"
    age=18
    location="Vizag"

    #Behaviour (Actions)
    def details(self):
        print(f'{self.name} is {self.age} years old and is {self.location} resident')

s1=Students()
print(dir(s1)) # dir is used to display attributes of class
print(s1.age,s1.name,s1.location)
s1.details()

print(s1.__class__)#returns class name of object
print(s1.__doc__)#returns docstring of class
print(s1.__dict__)#returns empty as we didnot have constructor(method)
#whatever objects we create its only same
s2=Students()
s2.name="Balaji"
s2.age=20
s2.location="Hyderabad"
s2.details()


#in the above case we want to modify the attributes such that we can create multiple objects with specific attributes and menthos.

class Students:
    """Students class with Actions"""
    def __init__(self,name,age,email_id,mobile_no):
        self.name=name
        self.age=age
        self.email=email_id
        self.mobile=mobile_no
    
    def profile(self,name,age,email_id,mobile_no):
        self.name=name
        self.age=age
        self.email=email_id
        self.mobile=mobile_no
    # to display the details of student
    def display(self):
        print(f'Student Name: {self.name}')
        print(f'Student Age: {self.age}')
        print(f'Student Email: {self.email}')
        print(f'Student Mobile: {self.mobile}')

#s1=Students()
#s1.profile("Balaji",23,"balaji@example.com",1234567890)
#s1.display()
#print(s1.__dict__)#returns dictionary of object with attributes and values
#s2=Students()
#s2.profile("Ganny",23,"ganny@example.com",9876543210)
#s2.display()
#print(s2.__dict__)#returns dictionary of object with attributes and values
s1=Students("yash",22,"yash@example.com",5555555555)
s1.display()



class Cars:
    """Cars class with basic details """
    def details(self,name,model,color):
        self.car_name=name
        self.car_model=model
        self.car_color=color
        print(f'{self.car_name} is {self.car_model} model and is {self.car_color} in color')

count=0
while count<3:
    fav_car=Cars()
    car_name=input("Enter your favourite car name: ")
    car_model=input("Enter your favourite car model: ")
    car_color=input("Enter your favourite car color: ")
    fav_car.details(car_name,car_model,car_color)
    count+=1

'''

