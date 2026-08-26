'''
1)Arthematic Operators:(+,-,*,/,%,)
-----------------------------------


2)assignment operators:(=,+=,-=,*=,/=,%=)
----------------------


+=:--> increment operator

a=0
print(a)
a+=5
print(a) -->output: 5


-=:-->decrement operator


a=67
a-=5
print(a) --->output: 26

*=:

c=2
c*=7
print(c) ---> output:14

/=:

c=4
c/=2
print(c) ---> output:2


%=:

c=10
c%=3
print(c)

3)comparision operators:(==,>=,<=,<,>!=)
---------------------------------------


a=5
b=9
print(a==b) #5=9 -->false
print(a!=b) #5!=9 --> true
print(b>a)  #9>5 -->true
print(b<a) #9<5 -->false

>=
--

num=10
num_2=9
print(num>=num_2) #true
print(num<=num_2) #false

4) logical operators:(and, or , not)
-----------------------------------

num=9
num_2=13
print(num >= num_2 and num<=10) #9>=13 and 9<=10 -->false
print(num <=num_2 and num<=10)  #9<=13 and 9<=10 -->true
print(num >= num_2 and num<10)  #9>=13 and 9<10  -->true
print(not(num >= num_2 and num<10))  #not(9>=13 and 9<10)  -->false

5)Identity operators:(Is, Is Not)
--------------------------------

a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a==b) #-->true == checks the values
print(a is b) #-->false , is checks both values and object location
print(a is not b) #-->true, reverse of is

6)MemberShip Operators:(in, not in)
-----------------------------------

nums = 'python is language'
print('y' in nums) --->true, checks y is in the input or not
print( 'i' not in nums) --->false , we have i in the input 

'''



