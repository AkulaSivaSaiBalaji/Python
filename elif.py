'''
elif: -->elif statement is used to check more possible condtions
-----

ex:
---
a=90
b=780
c=6700
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

task:
----
num=float(input('enter a '))
num_2=float(input())
user_option=int(input("enter \n1.add \n2.sub \n3.multiplycation: \n4.power"))
if user_option==1:
    print(num+num_2)
elif user_option==2:
    print(num-num_2)
elif user_option==3:
    print(num*num_2)
elif user_option==4:
    print(num**num_2)
else:
    print('invalid operation')


nested-if: -->if inside an if statement is called nested-if
----------

ex:
---
task:
----
app_details={'Pin':1234}
import random
user_pass = int(input('Enter your app password:'))
otp=random.randint(1000,9999) 
if app_details['Pin']==user_pass:
    print(otp)
    user_otp=int(input('enter otp:'))
    if user_otp==otp:
        print('welcome')
    else:
        print('incorrect otp')
else:
    print('incorrect pin')

task:
-----
num=int(input('Enter a number:'))
if num%==0:
    print(f'{num} is even')
else:
    print(f'{num} is odd') 


marks=int(input("Enter your marks:"))
if marks<=100:
    if marks>=90:
        print('+A')
    elif marks>=80:
        print('A')
    elif marks>=70:
        print('B+')
    elif marks>=60:
        print('B')
    elif marks>=50:
        print('C+')
    elif marks>=40:
        print('D')
    else:
        print('FAIL')
else:
    print('marks out of range')

'''

#prime number program
num=int(input('Enter a number:'))
if num>1:
    for i in range(2,num):
        if num%i==0: #every number is divisible by 1 and itself so performed a reverse logic
            print("not a prime number!!!")
            break #stops the loop of finding which numbers were dividing given number first one is enough
    else:
        print("prime number!!!")
else:
    print("enter any number other than one")
