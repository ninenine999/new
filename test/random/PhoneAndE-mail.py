'''
Created on 2017年6月21日

@author: admin
'''
import pyperclip,re
phoneRegex=re.compile(r'''(
    ((\d{3}|\(\\d{3}))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''',re.VERBOSE)

noNewlineRegex1=re.compile('.*',re.DOTALL)
x=noNewlineRegex1.search('Servaskdlfa ka lfa .\n  fak.\nskfa').group()
print(x)
