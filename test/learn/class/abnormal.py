'''
Created on 2017年6月20日

@author: admin
'''


try:#可能出错的代码
    num=100
    print(num)
except(NameError) as errmsg:#如果出现该错误，这里则执行
    print('产生错误了：%s'%errmsg)
else:#没有出错，则执行这个位置
    print('没有捕获到异常，')
finally:#无论是否有错误，均会执行。
    print('我一定会执行的哦')
    


try:
    print('---test---1---')
    print(num)
    open('123.txt','r')
    print('---test--2----')
except (IOError,NameError) as errmsg:#产生的错误
    print('请选择正确的文件',errmsg)