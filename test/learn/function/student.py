'''
Created on 2017年6月13日

@author: admin
'''
#1.展示功能
def showFuction():
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.遍历所有学生列表')
    print('6.退出系统')
#3.1如用户新增
def infnation():
    name=input('请输入姓名')
    age=input('请输入年龄')
    id=input('请输入ID')
    studentInfo={}
    studentInfo['name']=name
    studentInfo['age']=age
    studentInfo['id']=id
    return studengList.append(studentInfo)

#3.2删除
def deleteStu():
    a=int(print('请输入要删除的下标'))
    del studengList[a]
#3.3修改
def modifyStu():
    b=int(input('请输入要修改的下标'))
    name=input('请输入修改后的姓名')
    age=input('请输入修改后的年龄')
    id=input('请输入修改后的ID')
    studentInfo={}
    studentInfo['name']=name
    studentInfo['age']=age
    studentInfo['id']=id 
    studengList[b]=studentInfo
#3.4用户查询
def selectStu():
    b=int(input('请输入要查找的下标'))
    print(studengList[b])
#3.5遍历所有学生
def stundentLISt1():
    print('name   age    id')
    for temp in  studengList:
        print(temp)
#2.获取用户输入信息

studengList=[]

i=0
while i<10:
    showFuction()
    key=int(input('请根据上列功能序号'))
    
   
#3.根据输入信息判断功能
    if key==1:
        print('请输入学生信息（姓名、年龄、ID）')
        infnation()
    elif key==2:
        print('请输入需要删除的学生信息')
        deleteStu()
    elif key==3:
        print('请输入需要修改的学生信息')
        modifyStu()
    elif key==4:
        selectStu()
    elif key==5:
        print('遍历学生信息')
        stundentLISt1()
    elif key==6:
        exit1=input('亲真的要退出吗？yes/no')
        if exit1=='yes':
            break
    else:
        print('输入错误请重新输入')
