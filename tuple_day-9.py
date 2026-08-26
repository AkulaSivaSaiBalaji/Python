'''
Tuple:
-----

-->Tuple is collection of different datatypes that seperated by, and represented by ()

-->it is immutable

-->we can pass a tuple of values and that can be assinged to the variales , but it should match same number of variables and values inside the tuple

ex:
---
name,age,batch = ('Teja',34,6)
print(name,age,batch)

ex:
---
t=(1,'python',[3,4],(7,9))
print(t)


Indexing:
--------

ex:
---
t=(1,'python',[3,4],(7,9))
print(t[2])
print(t[2][1])


index():
-------
-->if the item is not present in the tuple , it will raise ValueError

ex:
---
t=(1,'Python',[3,4],(7,9))
print(t.index('python') #-->gives index no.
print(t.index('Python') #-->gives ValueError


len():
------

ex:
---
t=(1,'Python',[3,4],(7,9))
print(len(t)) #-->gives number of items present in the tuple



max():
-----
-->used to find max value in the tuple
-->all values in tuple must be numbers

ex:
---
so = (67,5,89,45)
print(max(so))#-->89 is the max value in

min():
-----
-->used to find min value in the tuple
-->all values in tuple must be numbers

ex:
---
so = (67,5,89,45)
print(max(so)) #-->5

count():
--------
-->count() used to count the number of occurances of a item in the tuple

ex:
---
so = (67,5,89,45,5,'py','py')
print(so.count('py'))


so = (67,5,89,45,5,'py','py')
do = (67,5,89,45)
print(so+do) #-->concatinates both tupless
'''
