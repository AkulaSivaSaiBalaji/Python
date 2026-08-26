'''
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}

print(data)
data['AC']=123456789
print(data)


update(): -->method is used to update a key, incase if the key is not present inside the dict then it will add that key:value
----------

syntax: --> dict.update({key:value})
-------
ex:
--
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}
data.update({'name':'sony'})
data.update({'ATMPIN':7899})
print(data)

-->there is another way to update a key

syntax: --> dict[key]=value
------
ex:
--

data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}

print(data)
data['AC']=123456789
print(data)


values(): -->values method is used to get all the values from the dict
--------

syntax: -->dict.values()
------
ex:
--
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}
print(data.values())



keys(): -->keys() method is used to get all the key from the dict
--------

syntax: -->dict.keys()
------
ex:
--
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}
print(data.keys())  #prints all the key values in dict


items(): -->items() method is used to get all the key, value pair  from the dict
--------

syntax: -->dict.items()
------
ex:
---
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}
print(data.items())  #prints all the key value pairs


clear(): -->clear() method is used to delete entire data from the dict
--------

ex:
---
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}
print(data)
data.clear()
print(data)

-->if you want to remove a particular key's value or a particular value using key
ex:
---
data = {
        'name':'Teja',
        'balance': 7000,
        'Adr':123456789684654,
        'PANC':'adkgfkjsbdk',
         2:[3,4,]}

del data['Adr']
print(data)
'''
