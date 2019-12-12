'''
Created on 2017年6月20日

@author: admin
'''
import pprint

spam={'name':'Pooka','age':5}
spam.setdefault('color','black')
print(spam)
spam.setdefault('color','white')
print(spam)
import pprint
message='It was'
count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1
pprint.pprint(count)