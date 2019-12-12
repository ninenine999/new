import requests
from lxml import etree

from lxml import html
#
# for i in range(0,6):
#     url = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_18374&page=10&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=6#J_main'
#     l = list(url)
#     l[70] = str(i)
#     # print(i)
#     url = ''.join(l)
#     pageContent=requests.get(url)
#     pageText = html.fromstring(pageContent.text)
# url='http://detail.zol.com.cn/cell_phone_index/subcate57_1673_list_1_0_1_2_0_1.html'
# pageContent=requests.get(url)
# pageText = html.fromstring(pageContent.text)
#
# for i in range(1, 61):
#     # print(i)
#     a = '//*[@id="plist"]/ul/li[1]/div/div[4]/a/em/text()'
#     l = list(a)
#     l[23] = str(i)
#     a = ''.join(l)
#     moblie = pageText.xpath(a)
#     print(moblie)
url="http://detail.zol.com.cn/cell_phone_index/subcate57_34645_list_1_0_1_2_0_3.html"
pageContent=requests.get(url)
pageText = html.fromstring(pageContent.text)

for i in range(1,60):
    # print(i)
    a = '//*[@id="J_PicMode"]/li[1]/h3/a/text()'
    l = list(a)
    l[24] = str(i)
    a = ''.join(l)
    moblie=pageText.xpath(a)
    print(moblie)
