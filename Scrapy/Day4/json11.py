import shengchengqi

#序列话dumps
import json
# info={'name':'wanyumie',
#       'age':27}
# f=open('text.txt','w')
# print(json.dumps(info))
# w=json.dumps(info)
# f.write(w)
# f.close()



#反序列话loads
# f=open('text.txt','r')
# data=json.loads(f.read())
# print(data['age'])

import pickle
#pickle
#pickle
# def sayhi(name):
#     print('hello',name)
# info={'name':'wanyumie',
#       'age':27}
#       # 'func':sayhi
# f=open('text.txt','wb')
# f.write(pickle.dumps(info))

# f=open('text.txt','rb')
# d=pickle.loads(f.read())
# print(d)

# import pickle
# # info={'name':'wanyumie',
# #       'age':27}
# # f=open('text.txt','wb')
# # pickle.dump(info,f)
#
# a=open('text.txt','rb')
# print(pickle.load(a))


#每次都只能用一次dumps，loads
# import json
# info={'name':'wanyumie',
#       'age':27}
# f=open('text.txt','w')
# f.write(json.dumps(info))
# info['age']='21'
# f.write(json.dumps(info))
#
#
# f=open('text.txt','r')
# json.loads(f.read())