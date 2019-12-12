'''
Created on 2017年6月20日

@author: admin
'''
from urllib import request
request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1497981054594&di=9db61e3bb511d59cb5a33e2989a75bfc&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20160829%2Fc6504f3c0f514517be1fd09e5281fcd0_th.jpg')
#with request.urlopen('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1497981054594&di=9db61e3bb511d59cb5a33e2989a75bfc&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20160829%2Fc6504f3c0f514517be1fd09e5281fcd0_th.jpg') as f:
   # date=f.read()#读取
    #print('status:',f.status,f.reason)
    #for k,v in f.getheaders():
       # print('%s,%s'%(k,v))
    #print('Date',date.decode('utf-8'))
