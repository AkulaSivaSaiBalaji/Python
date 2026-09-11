'''
Exception Handling:
------------------
--> This is the way of handling errors 
-->we can write any number of exception 

try:
----
-->The try block, where we can write code which may contain error
syntax:
    try:
        ----
        ----

except:
-------
-->this will handle error that are raised in try block

else:
-----
-->The else block will only execute if there are no errors in try block

finally:
-------
-->Finally execute the code inside it regardless any error present in try block

ex:
---
try:
    #print(5/0) #when this line executes it will go to ZeroDivisionError except and execte what inside it and exceutes and stops the progrm
    #print(num) when this line executes it will go to NameError except and execte what inside it and exceutes and stops the progrm
    print("Hello")
except ZeroDivisionError:
    print("Division by Zero error")
except NameError:
    print("Name not defined")
else:
    print("no error")
finally:
    print("Iam Bhasa.........Manik bhasa")


File handling:
--------------

-->the file handler is a object, which is used to create, update,read, and delete...


modes:
------

r: -->the (r) mode is used when the read() function is used

ex:
with open('demo.txt','r') as file:
    print(file.read())

w: -->
a
x

'''

with open('sai.txt','x') as file:
    file.write("This is python class no pulihora mixing")