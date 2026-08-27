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
'''
