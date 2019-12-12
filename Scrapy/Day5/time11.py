import time
print(time.time())#时间戳
print(time.localtime())#结果为UTC+8
a=time.localtime()
print(a.tm_year)
# print(time.gmtime(a))
print(time.gmtime())#gmtime 结果为UTC时区
a=time.localtime(891982771)
print(a.tm_year)
print(time.mktime(a))#转化为时间戳
print(time.strftime('%Y-%m-%d %H:%M:%S',a))#转代为格式化的字符串

print(time.strptime('2017-07-21 22:24:18','%Y-%m-%d %H:%M:%S'))
print(time.asctime(a))#转化为星期、月、日、小时、分钟、秒、年
print(time.ctime(4124414124))#转化为星期、月、日、小时、分钟、秒、年


import datetime
print(datetime.datetime)
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3))#当前时间加3天
print(datetime.datetime.now()-datetime.timedelta(3))#当前时间减3天
print(datetime.datetime.now()-datetime.timedelta(hours=3))#当前时间减3小时
print(datetime.datetime.now()-datetime.timedelta(minutes=3))#当前时间减3天


import random
print(random.random())#只能是0-1
print(random.randint(1,3))
print(random.randint(1,3))
print(random.randint(1,3))
print(random.randint(1,3))
print(random.randrange(1,3))
print(random.randrange(1,3))
print(random.randrange(1,3))
print(random.randrange(1,3))
print(random.randrange(1,3))

print(random.choice('ekldf ake ld faod'))
print(random.choice([1,421,421,521,1,1]))

print(random.sample([1,421,421,521,1,1],2))#随机取两位

print(random.uniform(1,3))#指定区间取随机数

items=[1,2,3,4,5,6,7]
random.shuffle(items)
print(items)#打乱验证码





