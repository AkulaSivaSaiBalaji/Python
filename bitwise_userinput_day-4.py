'''
Bit-wise operators: mainly deals with binary numbers
-------------------

&: bit-wise and
---------------

5 -->1010
3 -->0011

sprint(5&3) #output: 1 (0010)


|: bitwise or
------------

5-->0101
3-->0011
print(5|3) #output : 7 (0111)


^: bitwise XOR:(t:t--f, f:f--F, remaining all true)
--------------

5-->0101
3-->0011
5^3-->0110
print(5^3) -->output: 6(0110)

>>: right-shift:
----------------
5 -->0101
print(5>>2) output:0001 shifts 2 places right for 5(0101)

<<: left-shift:
---------------

5-->0101
print(5<<1) output: 10(1010) shifts 1 place left for 5(0101)-->10(1010)



input formatting:

-----------------

integer -->
-------

num=int(input('Enter a number:'))
print(num+2)

float -->
-----

num=float(input("Enter any decimal num: "))
print(num+3)

String -->
----------

so=input("Enter a String: ") #no need to specially mention str only needed for type casting
print(so, type(so))

List -->
--------


nums=list(map(int, input('Enter some numbers:').split()))  #list: creates list, map:used to map the enter values in list index places, split(): used to enter values in based on spaces dividing them by , 
print(nums)

tuple -->
---------

nums=tuple(map(int, input('Enter some numbers:').split()))
print(nums)


set -->
--------

nums=set(map(int, input('Enter some numbers:').split()))
print(nums)

data=eval(input('enter: ')) ---> to enter diffent types of data while giving input we use eval
print(type(data))


name = 'sai'
work = 'data analyst'
age = 23
print('My Name is' ,name, 'age is ',age)

print(f'My Name is {name} age is {age}') #--->f-string
print('my name is %s and im %d years old and iam currently working as a %s' %(name,age,work)) #--->moduls method

a=['sai','data analyst',23]
print('my name is %s and im %d years old and iam currently working as a %s' %(a[0],a[2],a[1]))
'''






