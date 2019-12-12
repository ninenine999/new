'''
Created on 2017年6月21日

@author: admin
'''
import re

phoneNumber=re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo=phoneNumber.search('my number is 415-111-4211.')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group())
