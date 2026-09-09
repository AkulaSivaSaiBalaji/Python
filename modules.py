'''
modules:
-------

-->A module is a python file(.py) that written using function, variables, operators, etc.

ex:
---
import problems
problems.add(12,30)


1.built-in-modules:
-------------------

-->the modules are developed by programmer and those comes with installation

ex:
---
math
-----
import math
a=math.pow(2,4)
print(a) -->16


os
--
ex:
---
import os
os.getcwd

sys
---
ex:
---
import sys
print(sys.path)
print(sys.version)

random
------
ex:
---
import random
print(random.randint(1000,9999))

importing specific function from the module
from  problems import add
add(1,2)

using alias name:
----------------
ex;
--
import problems as pb
pb.add(1,2)
'''