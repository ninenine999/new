import requests,re
from lxml import html
class jike(object):
    def linkt(self,mlink,total_num):
        pagelist=[]
        now_page=int(re.search('pageNum=(\d)',mlink,re.S).group(1))
        for i in range(now_page,int(total_num)+1):
            link=re.sub('pageNum=(\d+)','pageNum=%s'%i,mlink,re.S)
            i+=1
            pagelist.append(link)
        return (pagelist)

    def content(self,page):
        pageContent=requests.get(page)
        pageText=html.fromstring(pageContent.text)
        courseT=pageText.xpath('//*[@id="changeid"]/ul/li/div[2]/h2/a/text()')
        courseDetails=pageText.xpath('//*[@id="changeid"]/ul/li/div[2]/h2/a//@href')
        courseIntroduce=pageText.xpath('//*[@id="changeid"]/ul/li/div[2]/p/text()')
        courseTime=pageText.xpath('//*[@id="changeid"]/ul/li/div[2]/div/div[1]/dl/dd[1]/em/text()')
        courseStudent=pageText.xpath('//*[@id="changeid"]/ul/li/div[2]/div/div[1]/em/text()')
        return courseT,courseDetails,courseIntroduce,courseTime,courseStudent

    def wirtes(self,*args):
        for each in args:
            file=open('jikexueyuan.txt','a+')
            file.write(each)
            file.close()

course=jike()
m=course.linkt('http://www.jikexueyuan.com/course/?pageNum=1','10')
for each in m:
    course.wirtes('正在爬的链接：',each,'\n')
    print('正在爬取的页面是：%s'%each)
    title,details,introduce,courseTime,student=course.content(each)
    for i in range(len(title)):
        time=re.sub('\n\t\t\t\t\t\t\t','',courseTime[i],re.S)
        course.wirtes('正在爬取第',str(i+1),'条','\n','titile:',title[i],'\n','details:',details[i].strip('//'),'\n',
                      'introduce:',introduce[i].strip('\n\t\t\t'),'\n','time:',time,'\n','student',student[i],'\n','\n')
print('爬取完成，请查看')

