import  sys
f=open('yesterday2','r',encoding='utf-8')
f_new=open('yesterday2.bak','w',encoding='utf-8' )
find_str=sys.argv[0]
replace_str=sys.argv[1]
for i in f:
    if '123' in i:
        i=i.replace('123','mmmssk')
    f_new.write(i)
