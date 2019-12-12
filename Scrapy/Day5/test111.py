import random
#第一种办法
checkcode=''
for i in range(4):
    s=random.choice('0123456789qwertyuiopasdffgjklzxcvbnm')
    checkcode+=str(s)
print(checkcode)

#第二种办法,将数字转化为字母
checkcode=''
for i in range(4):
    current=random.randrange(0,4)
    if i==current:
        tmp=chr(random.randint(65,90))
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)
