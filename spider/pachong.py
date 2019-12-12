import requests,re
from lxml import html
def link(url):#单个链接下的具体内容
    links=requests.get(url)
    links.encoding = 'gb2312'
    # print(links.text)
    linksT = html.fromstring(links.text)
    linksN = linksT.xpath('/html/body/div/div/div/div/div[2]/h1/text()')#取标题
    linksD=linksT.xpath('/html/body/div/div/div/div/div/div[1]/div[1]/p/text()')#取内容
    x=str(linksN[0]).encode('utf-8')
    # print(x)
    # print(linksD)
    y=str()
    for m in range(len(linksD)):
        y+=linksD[m]
    # print(y)
    y.encode('utf-8')
    return x,y

def wirte(x):#写入文件
    f=open('内容.txt','a+',encoding='utf-8')
    f.write(x+'\n')
    f.close()

def souye(links):
    neirong=requests.get(links)
    neirongTree=html.fromstring(neirong.text)
    neirongTitle=neirongTree.xpath('//*[@id]/div/div[2]/h3/a/text()')#提取标题
    neirongLink=neirongTree.xpath('//*[@id]/div/div[2]/h3/a/@href')#提取链接

    neirongTime=neirongTree.xpath('//*[@id]/div/div[2]/div/div/span/text()')#提取时间
    return neirongTitle,neirongLink,neirongTime

neirongTitle,neirongLink,neirongTime=souye('http://www.iresearch.cn/')
for m in range(len(neirongTitle)):
    if re.findall('content(.*?)shtml',neirongLink[m],re.S) :
        title,rong = link(neirongLink[m])
        wirte(title.decode('utf-8'))
        wirte(neirongLink[m])
        wirte(neirongTime[m])
        wirte(rong)
        wirte('\n')
    else:
        continue






