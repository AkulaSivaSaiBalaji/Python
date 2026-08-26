'''
#indexing:
#--------
#positive -->0
#negitive -->-1


so=[1,2,3,4,'python']
print(so[-1])

#task:
#-----
all=[12,[1,'python',[1,4],(78,[6,7])],['java',78]]
print(all[-2][-1][-1]) #negitive indexing searches from backside starting with index -1,
print(all[1][3][1])    # positive indexing searches from begining starting with index 0

#task:
#-----
data_=['python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(data_[1][2][1][2])


#len():  this function is used to cal num of items in list
#------

data_=['python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(len(data_[1][2]))


#Slicing:
#--------



data=[1,2,3,4,5,6,7]
print(data[2:6])

#concatination:

a=[1,2]
b=[3,4]
print(a+b),


Methods:
--------

1)append(): append() will add new items at last index position
----------


go =[1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)
go.append(5)
print(go)
go.append([(1,2),'true',])
print(go)


2)extend(): extend will add the items into a list at last index position, but it will give each value in iterable value as one index inside the list,
-----------

-->it will not accpect non iterables, only string, list, tuple, set, dictionary, not numbers.

a=[1,2]
a.append([3,4])
print(a)
b=[1,2]
b.extend([3,4])
print(b)
go=[1,2]
go.extend('python')
print(go)
go.extend({'name':'sai'})
print(go)


3)pop(): pop() is used to remove items from the list and it will remove based on the index value 
-------

m=[1,2,3,4]
m.pop(3) #takes index position of the item we want to remove
print(m)
n=[1,2,3,4,'python']
n.pop(4)
print(n)


4)remove(): -->remove() will be able to delete items in list based on the value given inside it 
----------

-->only able to remove one value at a time

m=[1,2,3,4,5,'python']
m.remove('python')
print(m)
m.remove(5)
print(m)

'''

a='python programming'
a=list(a)
a.pop()
a.pop()
a.pop()
print(a)


