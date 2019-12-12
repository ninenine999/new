# date=open('yesterday.txt').read()
#
# print(date)
# f = open('yesterday2','r',encoding='utf-8')
# for index,line in enumerate(f.readlines()):
#     if index==9:
#         print('————————')
#         continue
#     print(line.strip())

# for i in range(5):
#     print(f.readline())

# f = open('yesterday2','r',encoding='utf-8')
# i=0
# for line in f:
#     i += 1
#     if i == 10:
#         print('---')
#     print(line)
# f.close()
# f = open('yesterday2','r',encoding='utf-8')
# print(f.tell())
# f.readline()
# f.readline()
# f.readline()
# print(f.tell())#打印当前的位置
# f.seek(0)#回到指定位置
# print(f.readline())
# print(f.fileno())
# print(f.flush())
# f = open('yesterday','w',encoding='utf-8')
# f.write('hello\n')
# f.flush()
# import  sys,time
# for i in range(10):
#     sys.stdout.write('#')
#     sys.stdout.flush()
#     time.sleep(0.2)

# f = open('yesterday2','a',encoding='utf-8')
# f.truncate(10)
# f = open('yesterday2','r+',encoding='utf-8')#读写
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.write('----')#只写到最后
# print(f.readline())
# f = open('yesterday2','w+',encoding='utf-8')#写到最后
# f.write('----')
# f.write('----')
# f.write('----')
# f.write('----')
# f.write('----')
# f.write('----')#只写到最后
# print(f.readline())
# f=open('yesterday2','wb')#二进制文件读写 rb读
# f.write('heloo world\n'.encode())
