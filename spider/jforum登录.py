import requests,re
from lxml import html
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

url='http://192.168.1.106:8089/jforum-2.1.9/user/login.page'
newurl='http://192.168.1.106:8089/jforum-2.1.9/jforum.page'
s=requests.session()
link=s.get(url)
n=type(link.cookies)
# print(link.headers)
# y=link.cookies.keys()#cookie读取
# m=link.cookies.values()
# c={}
z={c.name:c.value for c in link.cookies}
print(z)
for i in z.keys():
    print(i,z[i])
date={
    'module':'user',
    'action':'validateLogin',
    'returnPath':'http://192.168.1.106:8089/jforum-2.1.9/forums/list.page',
    'username':'admin',
    'password':'Pass1234',
    'redirect':'',
    'login':'登入'}
newhtmll=s.post(newurl,data=date)
print(newhtmll.cookies)


#发帖
index='http://192.168.1.106:8089/jforum-2.1.9/jforum.page'
fati='http://192.168.1.106:8089/jforum-2.1.9/jforum.page?module=posts&action=insert&forum_id=1'
bady='------WebKitFormBoundaryfa394dOkq52qqBGm'

datepost={
    'action':(None,'insertSave'),
    'module':(None,'posts'),
    'preview':(None,'0'),
    'forum_id':(None,'1'),
    'start':(None,''),
    'subject':(None,'希望发送成功，'),
    'addbbcode24':(None,'#444444'),
    'addbbcode26':(None,'12'),
    'helpbox':(None,'提示: 格式可以快速套用在选择的文字上'),
    'message':(None,'今天的任务就是发送成功吧'),
    'disable_html':(None,'on'),
    'attach_sig':(None,'on'),
    'notify':(None,'on'),
    'topic_type':(None,'0'),
    'poll_label':(None,''),
    'poll_option':(None,''),
    'poll_option_count':(None,'1'),
    'poll_option_1':(None,''),
    'poll_length':(None,'0'),
    'edit_attach_ids':(None,''),
    'delete_attach':(None,''),
    'total_files':(None,'1'),
    'file_0':(None,'Content-Type: application/octet-stream'),
    'comment_0"':(None,'')
}

headers = {'Proxy-Connection': 'keep-alive',
           'Content-Length': '2321',
           'Cache-Control': 'max-age=0',
           'Origin': 'http://192.168.1.106:8089',
           'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'content-type': 'multipart/form-data;boundary=----WebKitFormBoundaryfa394dOkq52qqBGm',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Referer':'http://192.168.1.106:8089/jforum-2.1.9/jforum.page?module=posts&action=insert&forum_id=1',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.8'}
index='http://192.168.1.106:8089/jforum-2.1.9/jforum.page'
fati='http://192.168.1.106:8089/jforum-2.1.9/jforum.page?module=posts&action=insert&forum_id=1'
# y=json.dumps(datepost)

n=s.post(index,files=datepost,headers=headers)
# print(n.request.body)
# print(n.headers)
