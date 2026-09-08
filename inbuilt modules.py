'''

Math:
-----
ex:
---
import math
print(math.sin(5))
print(math.pow(2,250))

random:
--------

import random
print(random.randint(100000,599999))
print(random.randrange(100000,599999))
a=['red','blue','yellow','orange','green']
print(random.choice(a))
random.shuffle(a)


platform:
---------

import platform
print(platform.system())
print(platform.processor())
print(platform.platform())
print(platform.python_compiler())

collections:
------------

import collections
data = collections.defaultdict(list) #will change the data type for which we passed inside of defaultdict
data['name'].append('sai')
data['age'].append(24)
print(data)


data time:
---------


from datetime import datetime
today=datetime.today()
print(today)
print(today.month)
print(today.hour)

#task: 
import random
number=random.randint(1,100)
#print(number)
attempts=3
first_prize=500
second1_prize=300
thrid_prize=200
while attempts>0:
    guess=int(input("enter a number between 1-100: "))
    if guess>0:
        if number==guess and attempts==3:
            print(f"you won!! your prize money is : {first_prize}")
            break
        elif number==guess and attempts==2:
            print(f"you won!! your prize money is : {second1_prize}")
            break
        elif number==guess and attempts==1:
            print(f"you won!! your prize money is : {thrid_prize}")
            break
        else:
            print(f"better luck next time :( you  have {attempts-1} attempts left")
    else:
        print("invalid number")
        break
    attempts-=1
'''
