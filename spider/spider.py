import requests,re
linke=requests.get('http://www.iresearch.cn/')
m=requests.utils.get_encodings_from_content(linke.text)#取网页的编码格式
linke.encoding='gb2312'
linkeText=linke.text
textQ=re.findall('g-news f-mt-auto(.*?)<!-- 资讯 end-->',linkeText,re.S)[0]#取列表这一块内容
textQL=re.findall('<h3><a href="(.*?)" target="_blank">(.*?)</a></h3>',textQ,re.S)#取出链接与标题
textTime=re.findall('<div class="time f-fr"><span>(.*?)</span></div>',textQ,re.S)#取发表时间
i=0
file=open('test.txt','w+')
for i in range(int(len(textQL))):
    print(textQL[i][0])#链接
    detailsLike=requests.get(textQL[i][0])#进入到链接的那一页
    detailsLike.encoding='gb2312'
    detailText=detailsLike.text
    print(detailText)
    print(textQL[i][1])#标题
    print(textTime[i])#发表时间
    file.write(textQL[i][0]+'\n'+textQL[i][1]+'\n'+textTime[i]+'\n')#简单写入文件




# linkeT=requests.get('http://www.iresearch.cn/include/pages/redis.aspx?specialId=399&lastId=news.270189')
# data={
#     'specialId':'399',
#     'lastId':'news.270199'
#     }
# likeT_get=requests.get('http://www.iresearch.cn/include/pages/redis.aspx?',params=data)
# print(likeT_get.url)
# likeT_get.encoding='gb2312'
# LikeText=likeT_get.text
# print(LikeText)


