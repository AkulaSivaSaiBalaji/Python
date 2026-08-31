'''
#1'st problem
a=int(input('enter first number: '))
b=int(input('enter second number: '))
c=int(input('enter third number: '))
if a==b==c:
    print('all are equal')
elif a==b or b==c or a==c:
    print('two are equal')
else:
    print('not all are equal')
'''
'''
#2nd problem
a=input('enter your character: ')
if a.isupper():
    print('the character is uppercase')
elif a.islower():
    print('the character is lowercase')
elif a.isdigit():
    print('the character is digit')
else:
    print('the character is special character')
'''
'''
#3rd problem
a=int(input('enter your number: '))
count=0
while a >0:
    a=a//10
    count=count+1
print(f'given number is a {count} digited number')
'''
'''
#4th problem
a=int(input('enter your desired number table: '))
b=int(input('enter your range of table: '))
for i in range(1,b+1):
    print(f'{a}*{i}={a*i}')

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
    print("enter any number greater than one")

star='*'
a=20
for i in range(1,a+1):
    print(star*i) 



star=int(input('enter your desired number of rows: '))
for i in range(1,star+1):
    for j in range(1,i+1):
        print('*', end=' ')
    print()
'''
'''
star=int(input('enter your desired number of rows: '))
count=0
for i in range(1,star+1):
    for j in range(1,i+1):
        count+=1
        print(count, end=' ')
    print()
'''
'''
#printing the length of words in a given text
text='python is easy programming language'
words=text.split()
print(type(words))
print(len(words))
'''
'''
digits_=(1,2,3,1,5,5,6,7,8,9,9 )
dup=set()
for i in digits_:
    if digits_.count(i)>1:
        dup.add(i)
dup=tuple(dup)
print(dup)
'''

'''
words='python is simple programming language'
word=words.split()
print(len(word))
'''

'''
word=list(map(str, input('enter your sentence: ').split()))
print(len(word))
'''
'''
for i in range(1,6):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(1,6):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print()

count=1
for i in range(1,5):
    for j in range(i):
        print(count, end=' ')
        count=count+1
    print()

for i in range(1,6):
    for j in range(i):
        print(chr(97+j), end=' ')
    print()

a=list(map(int,input('enter the numbers in the list').split()))
b=len(a)
gratest_number=0
for i in range(b):
    if gratest_number<a[i]:
        gratest_number=a[i]
print(gratest_number)
'''

#perfect number 
num=int(input('enter your number to check if it is a perfect number or not: '))
added_num=0
for i in range(1,num):
    if num%i==0:
        added_num=added_num+i
if num==added_num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')