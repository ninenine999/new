modname='aa'
#from lib import aa
# lib=__import__('lib.aa')
# ss=lib.aa.C()
# print(ss.name)

import importlib
ss=importlib.import_module('lib.aa')
yy=ss.C()
assert type(yy.name) is str
print(yy.name)