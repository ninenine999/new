'''
Created on 2017年6月21日

@author: admin
'''
import re
from turtledemo.clock import datum
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('cell:442-224-2231 work:212-224-2411')
s=mo.group()
print(s)
mo=phoneNumRegex.findall('cell:442-224-2231 work:212-224-2411')
print(mo)
xmasRegex=re.compile(r'\d'+'\s\w')

vowelRegex=re.compile(r'[中文]')
y=vowelRegex.findall('练习练习 中文中文的正则匹配哦')
print(y)

beginWithHello=re.compile(r'^Hello')
n=beginWithHello.findall('HelloHello world')
print(n)

beginWithHello=re.compile(r'^Hello')
n=beginWithHello.findall('helloHello world')
print(n)

beginWithHello=re.compile(r'Hello$')
n=beginWithHello.search('sss sdfHello')
print(n)


beginWithHello=re.compile(r'^Hello$')
n=beginWithHello.search('Hello')
print(n)

beginWithHello=re.compile(r'.友')
n=beginWithHello.findall('朋友你好吗？小友在吗？？你是我的好友吗？')
print(n)
beginWithHello=re.compile(r'First Name:(.*)Last Name:(.*)')
n=beginWithHello.findall('First Name: 朋友你好吗？小友在吗？？Last Name:你是我的好友')
print(n)
beginWithHello=re.compile(r'<.*?>')
n=beginWithHello.search('<To serve man > for dinner.>')
print(n)
beginWithHello=re.compile(r'<.*>')
n=beginWithHello.search('<To serve man > for dinner.>')
print(n)


noNewlineRegex=re.compile('.*')
x=noNewlineRegex.search('Servaskdlfa ka lfa .\n  fak.\nskfa').group()
print(x)

noNewlineRegex1=re.compile('.*',re.DOTALL)
x=noNewlineRegex1.search('Servaskdlfa ka lfa .\n  fak.\nskfa').group()
print(x)


m=re.compile('robocop', re.I)#不区分大小写
n=m.findall('Robocop fa df lsdf robocop')
print(n)


namesRegex=re.compile(r'Agent \w+')
y=namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob')
print(y)

namesRegex=re.compile(r'Agent (\w)\w*')
y=namesRegex.sub('\1***','Agent Alice gave the secret documents to Agent Bob')
print(y)


Data=(
    'Mountain View,CA94040',
    'SunnyVale,CA',
    'LosAltos,94023',
    'Cupertino 95014',
    'Palo Alto　CA')
for i in Data:
    print(re.split(', |(?=(?:\d{5}|[A-Z]{2}))',i))
