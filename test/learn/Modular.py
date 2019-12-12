'''
Created on 2017年6月8日

@author: admin
'''
#！usr/bin/python
#FILENAME:using_sys.py
import sys
from _ast import __name__
from _sqlite3 import version
print('The command line argenuments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is',sys.path,'\n')

#!/usr/bin/python
# Filename: using_name.py


#!D:\python\test\learn
#Filename:mymodule.py
import keyword
print(keyword.kwlist)




