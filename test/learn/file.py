'''
Created on 2017年6月21日

@author: admin
'''
import os
print(os.name)#操作系统
print(os.environ)#环境变量
print(os.environ.get('path'))#获取path环境变量


f=os.path.abspath('.')#查当前目录的绝对路径
print(f)
os.path.join('D:/python/test/learn','testdir')

import pickle
d=dict(name='BOb',age=20,score=88)
s=pickle.dumps(d)
print(s)
reborn=pickle.loads(s)
print(reborn)