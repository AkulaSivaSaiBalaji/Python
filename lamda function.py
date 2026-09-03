'''
lambda function:
---------------
-->lambda function is a small anonymous function.
-->lambda can take n number of arguments but can only have one expression.
-->the function is definied by using the keyword lambda.

ex:

add=lambda a,b,c: a+b+c
print(add(10,20,30))

ex:
---
add=lambda a,b,c: a+b+c
a=10
b=10
c=30
print(add(a,7,30))

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
grater = lambda x,y: x if x>y else y
print(grater(a,b))

grater = lambda x,y: x>y
if grater(10,20):
    print("10 is greater than 20")
else:
    print("20 is greater than 10")

cube=lambda x:x**3
print(cube(10))


filter:
------

-->filter() function will perform only on an selected elements of iterables.

syntax: -->filter(lambda arguments:expression,iterable)

nums=[1,2,3,4,5]
data=filter(lambda a:a%2==0,nums)#filter function is used to filter the data based on the condition provided in the lambda function.
print(list(data))

maps:
-----
--> map() function will perform the operation on all the elements of iterables.
syntax: -->map(lambda arguments:expression,iterable)

ex:
---
nums=[1,2,3,4,5]
add=map(lambda a:a+10,nums)#map function is used to perform the operation on all the elements of the iterable.
print(list(add))


from functools import reduce #should be imported to use reduce function.
nums=[1,2,3,4,5]
add=reduce(lambda a,b:a+b,nums)#reduce function is used to perform the operation on all the elements of the iterable and return a single value.
print(add)
add=reduce(lambda a,b:a*b,range(1,6))#reduce function is used to perform the operation on all the elements of the iterable and return a single value.
print(add)
'''
