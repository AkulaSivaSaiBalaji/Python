'''
List comprehension:
------------------
-->List comprehension is the shortest form of syntax to create a new list

syntax:--> [expression loop condition] 
syntax:--> [expression condition else loop] #if you want to use else also

ex:
---
old=(1,2,3,5,8)
new=[i for i in old]
print(new)

ex:
---
old=(1,2,3,5,8)
new=[i for i in old if i%2==0]
print(new)

nested comprehension:
--------------------

-->using list comprehension generating list inside list

ex:
---

any=[[i*j for i in range(1,6)] for j in range(1,10)]
print(any)

ex:
---
of=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

any=[a for i in of for a in i]
print(any)

generator:
----------
--> A generator is a special function which generates one value at a time

ex:
---
def all():
    for j in range(1,10):
        yield j
j=all()
print(next(j))
print(next(j))
print(next(j))
'''