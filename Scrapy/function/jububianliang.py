def chang_name(name):
    print('before change',name)
    name='alex li'
    print('afte change',name)
name='alex'
chang_name(name)
print(name)

#递归函数内部可以调用其它函数
#递归必须要有一个明确的结束条件、每次进入更深一层递归时，问题规模相比上次递归都应有所减少、递归效率不高，递归次过多会导
#致stack溢出
# def calc(n):
#     print(n)
#     if int(n/2)>0:
#         return calc(n/2)
#     print('->',n)
# calc(10)
def add(x,y,f):
    return f(x)+y
res =add(-3,1,abs)
print(res)