'''
Created on 2017年6月8日

@author: admin
'''
def fun(a,b=5,c=10): #这被称作 关键参数 ——我们使用名字（关键字）而不是位置
    print('a is ',a ,'b is',b,'c is ',c)
fun(3,37)
fun(10,c=50)
fun(c=30,a=20)

def num(x,y):  #return语句
    if x>y:
        return(x)
    else:
        return (y)

print(num(20, 30))


def printMax(x,y):
    '''Prints the maxinum of two numbers
        The two values must be integers'''
    x=int(x)
    y=int(y)
    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printMax(3, 5)
#print (printMax._doc_) 

