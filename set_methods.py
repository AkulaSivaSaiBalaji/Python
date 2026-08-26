'''
set{}: -->A set is an unordered collection of unique elements.
------
ex:
----
a = {10, 20, 30, 40}

print(a)

union(): -->
-------

ex:
---
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B) #prints combined set of two sets

print(A.union(B))

intersection():
-------------

ex:
---

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B) #prints the set contains common elements in both sets
print(A.intersection(B))


difference():
------------

ex:
---
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B) -->{1,2,3} #removes all the elements in A which are also present in B and prints remaining elements in A.

Symmetrical Difference():
-------------------------
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B) -->{1,2,3,6,7} #will print Elements that are in either A or B, but NOT in both.


add(): -->add() method will add only one element at a time
-----

syntax -->set.add(element)

ex:
---

data_={1,2,3,4}
print(data_)
data_.add(7)
print(data_)


update(): -->we can add more than one element by using update, it only accepcts only iterables
--------
syntax: -->set1.update(set2), set.update([elements])

data_={1,2,3,4}
data_.update([8,9])
print(data_)
nums={5,6,7}
data_.update(nums)
print(data_)
#data_.update(10) #throws error since update ACCPECTS only iterables
#print(data_)
data_.update((10,11,12))
print(data_)

remove(): -->remove() method will del the given element from the set, if item not present in the set it will throw error.
--------
syntax: -->set.remove(element)
------

data_={1,2,3,4}
data_.remove(4)
print(data_)
#data_removes(5)#throws error sincev 5 is not in our set
#print(data_)

discard(): -->discard() method will del the given element from the set, if item not present in the set it will not throw any error, simpilly display the given set.
----------
syntax(): -->set.discard(element)
---------

ex:
--
data_={1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(2,3)


clear(): -->the method is used to del all elements from the set and it will return empty set.
--------
syntax: -->set.clear()

data_={1,2,3,4}
print(data_)
data_.clear()
print(data_)
'''
data_={1,2,3,4}
data_.clear()
print(data_)
del a
print(data_) #completely deletes object too


