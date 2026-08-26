'''
if statement:
-------------

-->if condition become true, then it will execute inside block of code
-->incase it become false, then it will never enter into inside block

ex:
---
age=19
if age>=18: #condition satisfies of enters inside if block
    print("eligible to vote")
print(age)

age=15
if age>=18: #condition not satisfies so not entering if block
    print("eligible to vote")
print(age)


if-else:
-------
-->else for if statement is a fall-back statement, incase if condition is false then else block executes

ex:
---
age=15
if age>=18: 
    print(f'you are {age} eligible to vote')
else:
    print(f'your {age} ,not eligible to vote, wait for {18-age} years to vote')
