'''
Created on 2017年6月21日

@author: admin
'''
f=open('C:/Users/admin/Documents/112.txt','r')
print(f.read())
f.close


with open('C:/Users/admin/Documents/112.txt','r') as f:
    for line in f.readlines(1):
        print(line.strip())
