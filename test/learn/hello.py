classmates = ['Michael', 'Bob', 'Tracy']
classmates.insert(1, 'wang')
classmates.pop(-1)
classmates[0]='xin'
x =('1','2','3',['6','7'])
x[3][0]='a'
print(classmates,x)



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])


age =3
if age>=18:
    print('you age is',age)
    print('adult')
else:
    print('you age is',age)
    print('teenager')
    
    
    
    
age=3
if age>18:
    print('adult')
elif age>8:
    print('teenager')
else :
    print('kid')
    

'''y=input('birth:')
birth=int(y)
if birth>10:
    print('00前')
else:
    print('00后')'''
    
w=input('weight-kg')
weight=float(w)
h=input('height-m')
height=float(h)
import math
height=math.pow(height,2)
bmi1=weight/height
if bmi1>32:
    print('严重肥胖')
elif bmi1>28:
    print('肥胖')
elif bmi1>25:
    print('过重')
elif bmi1>18.5:
    print('正常')
else: 
    print('过轻')
    
    
    
name1=['x','y','z']
for name in name1:
    print(name)