'''
Created on 2017年6月11日

@author: admin
'''
for i in range(10):  
    s=''  
    for j in range(1,i+1):  
        s+=str(j)+'*'+str(i)+'='+str(j*i)+'\t'  
    print(s)