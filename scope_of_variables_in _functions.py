'''
Scope of variables in functions:
-------------------------------
1.Local variables:
-----------------
-->A variable that is defined inside a function is called a local variable. It can only be accessed within that function and is not visible outside of it.

ex:
---
def display():
    a = 'sai'   #Local variable
    print(a)

display()
print(a)  # This will raise an error because 'a' is not defined in the global scope

2.Global variables:
-------------------
-->A variable that is defined outside a function is called a global variable. It can be accessed from anywhere in the program.

ex:
---
a = 'balaji'  # Global variable

def display():
    a = 'sai'   #Local variable
    print(a) #This will print 'sai' because the local variable 'a' is defined within the function and takes precedence over the global variable with the same name.

display()
print(a)  # This will print 'balaji' because 'a' is defined in the global scope

global keyword:
----------------
-->global is a keyword used to reaccess new values to a variable that was already defined outside the function the function call. It allows you to modify the value of a global variable from within a function.

ex:
---
a=90
print(a)  # This will print 90 because 'a' is defined in the global scope
def display():
    global a  # This tells Python that we want to use the global variable 'a' instead of creating a new local variable
    a = 100   # This will modify the global variable 'a'
display()
print(a)  # This will print 100 because we modified the global variable 'a' within the function

passing by value:
-------------------
-->giving the value of a variable to a function is called passing by value. The function receives a copy of the variable's value, and any changes made to the parameter inside the function do not affect the original variable.

def even_odd(num=20):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
even_odd(10) #passing by value to the function


Recurrsive function:
-------------------

-->the function calling itself until the base condition is met.

ex:
---
def fact(a):
    if a==1 or a==0:
        return a
    else:
        return a*fact(a-1)

print(fact(2))
'''