
'''
Indexing:
---------


Negitive indexing
------------------

Negitive indexing sdtarts from -1 index

syntax: print(variable[negitive index position])
-----

text= 'python'
print(text[-1]

task
----
txt='Python is a programming language'
print(txt[-15])


len():
-----

-->len() is a built-in function that is used to get number of char present in a string.
syntax: -->len(variable_name)
------

txt='Python is a programming language'
print(len(text)) -->output:32


Slicing: -->slicing is used to access the particular part from the string 
-------
syntax: -->variable_name[start:end]
-------

ex:
---
txt='Python is a programming language'
print(txt[12:23]) #output: progrmming
print(txt[12:]) #output: programming language
print(txt[:23]) #output: Python is a programming

text='madam'
print(text[::-1] -->reverses the string

upper(): used to convert all small char into cap
-------
txt='Python is a programming language'
print(txt.upper())


lower(): used to convert all caps char into small char
-------
txt='Python is a programming language'
print(txt.lower())

index(): -->used to know the index position of an char 

txt='Python is a programming language'
print(txt.index('i')) #-->7
print(txt.index('i',9)) #-->20
print(txt[7]) #-->i

replace() -->used to replace old substring with new substring
--------

txt='Python is a programming language'
print(txt.replace('Python','Java'))


split(): -->this method is used to seperate string based on the given substring and gives output in list form
--------
txt='Python is a programming language'
print(txt.split(' '))

#task: count all words in given 
txt='Python is a programming language'
all=txt.split(' ')
print(len(all))

count(): 
-------
syntax: variable_name('sub-string', start index, end index)
 
txt='Python is a programming language'
print(txt.count('a',2,12))
'''
