'''
default arguments: -->The default arguments where the function will only consider the data at calling function even though data
-----------------     present at def line. If the data is not present at calling function then it will consider the data present at def line.
                      

ex:
---
def feb(num,num2):
    print(num+num2)

feb([1,3],[5,6])


def data(a=8,b=9):# both a and b  are default parameters
    print(a+b)
data(1,2) #it will take the values of a and b as 1 and 2 respectively
data() #it will take the default values of a and b as 8 and 9 respectively

def prime(num=3):
    
    for i in range(1,num+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,"is prime number")

num=int(input("Enter the number:"))
prime(num)

def number_prime(num=3):
    if num>=1:
        for i in range(1,num):
            if num%i==0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print('enter number greater than 1')

num=int(input("Enter the number:"))
number_prime(num)


keyword arguments: 
-----------------
-->Keyword arguments are sending arguments in a pair(a=2),and the order is not considered while sending the data to the function.

ex:
---
def data(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data(name='sai',age=22,batch='python',location='hyderabad')

variable length arguments:
--------------------------
--> Adding a(* call it as args) before a variable at parameter we can pass tuple of arguments and can be access with indexing.

ex:
---
def all(*name): #here *name is a variable length argument which can take any number of arguments and store them in a tuple.
    print(name)
all('siva','sai','balaji')

keyword length arguments:
---------------------------------
--> Adding a(** call it as kwargs) before a variable at parameter we can pass dictionary of arguments and can be access with key values.
ex:
---
def details(**data): #here **data is a keyword length argument which can take any number of keyword arguments and store them in a dictionary.
    print('',data.keys(),'\n',data.values())
details(name='siva',age=22,location='hyderabad')

return: -->return keyword used inside the function, once the return is executed means it will get back to the calling
------     function with certain values.

ex:
---
def dif(a,b):
    return a-b
print(dif(10,5))
'''