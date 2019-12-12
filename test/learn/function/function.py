from threading import _newname
def disPlayMenu1():
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查询名片')
    print('5.退出系统')
def getChoice1():
    selectedKey=int(input('请输入序号'))
    return selectedKey
def printInf(nameList1):
    print('------------------------')
    for temp in nameList1:
        print(temp)
    print('------------------------')
def deletenamelist(nameList2):
    print('------------------------')
    nameList2.remove(y)
    print(nameList2)
    print('------------------------')
def modify(namelist3):
    print('------------------------')
    n=input('请输入要修改的数据')
    f=namelist3.index(n)
    m=input('请输入新值')
    namelist3[f]=m
    print(namelist3)

    
nameList=[]
i=0
while i<10:
    disPlayMenu1()
    x=getChoice1()
    if x==1:
        print('添加名片')       
        name1=input("请输入名字")
        nameList.append(name1)
    elif x==2:
        print('删除名片')
        y=input('请输入要删除的数据')
    elif x==3:
        print('修改名片')
    elif x==4:
        print('查询名片')
        printInf(nameList)
    else :
        print('退出系统')












        