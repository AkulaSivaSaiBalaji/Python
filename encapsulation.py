'''
OOP---> Encapsulation,Inheritance,Polymorphism,Abstraction

Encapsulation:
-------------

It is one of the key features of OOP, it binds(bundles) the data(attributes and methods) into a single class.IT also provides 
specific accessibility as Public,Private,Protected attributes and methods.

Public attributes --> these are defines inside the class and can be modified outside the class.

class Users:
    """Users Data"""
    def __init__(self,name):
        self.user=name #public attribute
    def details(self):
        print(f'User name is {self.user}')

user1=Users("Balaji")
user1.details()
user1.user="yashwanth" #modifying public attribute outside the class
user1.details() 

Protected attributes --> these are defines inside the class and can be modified outside the class but with a warning.
-------------------

class Users:
    """Users Data"""
    def __init__(self,name,_otp):
        self.user=name #public attribute
        self._otp=_otp #protected attribute
    def details(self):
        print(f'User name is {self.user} and otp is {self._otp}')

user1=Users("Balaji", "123456")
user1.details()
user1._otp="654321" #modifying protected attribute outside the class
user1.details()

Private attributes --> in this case we make the attribute name with doubleleadingunderscore(__)
in very specific where the attribute need not be accessed directly such as we make it as __var
python breaches it ny name mangling and makes it as _classname__varname, so that it can be accessed outside the class but with a warning.


class Users:
    """Users Data"""
    def __init__(self,name,_otp,__password):
        self.user=name #public attribute
        self._otp=_otp #protected attribute
        self.__password=__password #private attribute
    def details(self):
        print(f'User name is {self.user}')

u1=Users("Balaji", "123456","balaji@123")
u1.details()
print(u1.user) #accessing public attribute outside the class
print(u1._otp) #accessing protected attribute outside the class
#print(u1.__password) #accessing private attribute outside the class but it will give error as it is private attribute
print(u1._Users__password) #accessing private attribute outside the class



class Users:
    """Users Data"""
    def __init__(self,name,_otp,__password):
        self.user=name #public attribute
        self._otp=_otp #protected attribute
        self.__password=__password #private attribute
    #to make the private attribute accessible outside the class we can create a method inside the class to access 
    #usiing getter 
    def get_password(self):
        return self.__password
    #to modify the private attribute outside the class we can create a method inside the class to modify using setter
    def set_password(self,new_password):
        if len(new_password)<6:
            print("Password should be minimum 6 characters")
        else:
            self.__password=new_password
            print("Password updated successfully")
            return self.get_password
    def details(self):
        print(f'User name is {self.user}')

p=Users("Balaji", "123456","admin@123")
print(p.user) #accessing public attribute outside the class
print(p._otp) #accessing protected attribute outside the class
print(p.get_password()) #accessing private attribute outside the class
p.set_password("bala") #modifying private attribute outside the class but it will give warning as it is less than 6 characters
p.set_password("balaji@123") #modifying private attribute outside the class
print(p.get_password()) #accessing private attribute outside the class after modification

p2=Users("Yashwanth", "654321","yash@123")
p2.set_password("yash") #modifying private attribute outside the class but it will give warning as it is less than 6 characters
p2.set_password("yashwanth@123")
print(p2.get_password()) #accessing private attribute outside the class after modification


#use setter and getter methods for both protected and private attributes, you can also have Public attributes



Inheritance:
-----------
It is one of the key features of OOP, which helps in acquring or reusing the properties (attributes,methods) from one class to 
another class. 

class BaseClass:
    """Base class"""
    statements
    ..........
class DerivedClass(BaseClass):
    """Derived class"""
    statements
    .............


#social media login example
class Users:
    """Users details"""
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    #initial case we just display
    def full_name(self):
        return self.fname+" "+self.lname

class User_v1(Users):
    """Updating user name"""
    def update_name(self,full_name):
        return full_name.title()

user1=User_v1("siva sai","balaji")
print(user1.full_name()) #inherited method from base class
print(user1.update_name("siva sai balaji")) #updated name
'''

#task
class SamosaSecurityOfficer:

    def __init__(self, name, samosa_count, secret_samosa_code):
        # Public attribute
        self.name = name

        # Protected attribute
        self._samosa_count = samosa_count

        # Private attribute
        self.__secret_samosa_code = secret_samosa_code

    # Protected attribute - Getter
    def get_samosa_count(self):
        return self._samosa_count

    # Protected attribute - Setter
    def set_samosa_count(self, count):
        self._samosa_count = count

    # Private attribute - Getter
    def get_secret_samosa_code(self):
        return self.__secret_samosa_code

    # Private attribute - Setter
    def set_secret_samosa_code(self, code):
        self.__secret_samosa_code = code

#public

officer = SamosaSecurityOfficer("Yashaswi",10,"SAMOSA-007")
print(f"Officer Name: {officer.name}")
officer.name = "Super Yashaswi"
print(f"Updated Name: {officer.name}")
print(f"Samosas in Security: {officer.get_samosa_count()}")
officer.set_samosa_count(25)
print(f"Updated Samosas: {officer.get_samosa_count()}")



# private

print(f"Secret Code: {officer.get_secret_samosa_code()}")
officer.set_secret_samosa_code("SAMOSA-999")
print(f"Updated Secret Code: {officer.get_secret_samosa_code()}")