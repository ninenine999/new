class School():
    #有属性为地址，学校名称
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress
    def newSchool(self):
        print('学校名字%s,学校地址%s'%(self.name,self.adress))
class Teacher(School):
    def __init__(self,name,adress,TeacherName):
        super(Teacher,self).__init__(name,adress)
        self.TeacherName=TeacherName
class Student():
    def __init__(self,StudentName,StudentAge):
        self.StudentNmae=StudentName
        self.StudentAge=StudentAge
class Class():
    def __init__(self,ClassNum):
        self.ClassNum=ClassNum
class Course():
    def __init__(self,CourseName,Money):
        self.CourseName=CourseName
        self.Money=Money

School1=School('成都商学院','四川成都华阳')
School1.newSchool()

School2=School('Python','上海')
School2.newSchool()