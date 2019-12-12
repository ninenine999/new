import requests
from lxml import html
ly=requests.get('http://www.iresearch.cn/')
ly.encoding='gb2312'
tree = html.fromstring(ly.text)
root = tree.xpath('//*[@id]/div/div[2]/h3/a/text()')#提取文本
rootl = tree.xpath('//*[@id]/div/div[2]/h3/a/@href')#提取属性
roott=tree.xpath('//*[@id]/div/div[2]/div/div/span/text()')#提取时间
file=open('xmltest.txt','w+')
for i in range(len(root)):
    # print(root[i])
    # print(rootl[i])
    # print(roott[i])
    # file.write('标题:'+root[i]+'\n'+'链接:'+rootl[i]+'\n'+'时间:'+roott[i]+'\n'+'\n')
    links=requests.get(rootl[i])
    links.encoding='gb2312'
    linksT=html.fromstring(links.text)
    linksN=str(linksT.xpath('/html/body/div/div/div/div/div[2]/h1/text()'))#取标题
    linksD = str(linksT.xpath('/html/body/div/div/div/div/div/div[1]/div[1]/p/text()'))  # 取内容
    file.write('标题:'+root[i]+'\n'+'链接:'+rootl[i]+'\n'+'时间:'+roott[i]+'\n')
    y = str()
    f=open('内容.txt','wb+')
    for m in range(len(linksD)):
        y+= linksD[m]
    x=y.encode('utf-8')
    print(f.read())
    print(y)
