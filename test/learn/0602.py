'''
Created on 2017年6月2日

@author: admin
'''
L = ['Bart', 'Lisa', 'Adam']
n=0
x=0
while n<3:
    n=n+1
    print('hello,'+L[x],end='')
    x=x+1


d={'Michael':95,'Bob':75,'Tracy':85}
print('\n\'Michael\'%s'%d['Michael'])
print('thomas' in d)

y={'Jack':90}
y['Jack']=80
print(y['Jack'])