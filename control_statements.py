'''
for loop: --> for loop is used to iterate over a sequence or iterable datatypes
--------


nums=[12,3,5,78]
for num in nums:
    print(num)

    
else in for loop: --> unlike if-else, else block in for statement is executed after completion of all iterations of for loop. If the for loop is terminated by a break statement, the else block will not be executed.
----------------
ex:
---
nums='python'
for num in nums:
    print(num)
else:
    print('for loop is completed')


break: --> break statement is used to terminate the loop when a certain condition is met.    
-----------------

nums=[1,2,3,4,5]
for num in nums:
    print(num)
    if num==3:
        break # breaks the for loop when num is equal to 3

            
task: write a program to check whether the numbers in the list are even or odd using for loop.
----- 
val=[1,2,3,4,5,8,9]
for i in val:
    if i%2==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

        
continue: -->the continue is a keyword used to skip the current iteration based on the condition.
---------

ex:
---
nums=[1,2,3,4,5,8,9]
for num in nums:
    if num==5:
        continue # skips the current iteration when num is equal to 5
    print(num)

    
pass: -->A pass is called as space holder, that is used after statements like (if, for, else,) not to raise any error
-----

for i in range(1,11):
    if i==15:
        print(i)
    else:
        pass #without pass statement, it will raise an error because there is no statement after else block.

assert: -->assert is a keyword used to check the condition, in case the condition is false,it will raise the error(AssertionError) and the message can be printed after comma.
-------

ex:
----
age=15
assert age>=18, 'you are not eligible to vote' # if the condition is false, it will print the message in assertion error message.
print('you are eligible to vote')

num=1
while num<5:
    print(num)
    num+=1

1)even or odd 
2)remove duplicates from list
3)armstrong number(power of digits)
4)number of vowels in a string
5)count the numer of words in a string
'''

a=list(map(str, input("enter your string: ").split()))
print(f'Total Number of words in given string: {len(a)}')

a=153
while a>0:
    b=a%10
    c=b**3
    a=a//10
    print(c)