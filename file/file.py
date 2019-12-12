import xlwt
import  jieba

gift ={'告白情书':20,
       '可爱萝莉':100,
       '浪漫玫瑰':990,
       '绚丽烟花':1800,
       '兰博基尼':5000,
       '豪华邮轮':9900,
       '一生一世':13140,
       '豪华飞机':52000,
       '丘比特之箭':500,
       '花好月圆':99999,
       '冬季恋歌':131400}


excelname = 'F:\yami\jmeter\intermediate_test.xls'
fopen = open('F:\yami\jmeter\intermediate_test.txt','r')
words = fopen.readlines()
counts = {}     # 通过键值对的形式存储词语及其出现的次数

jieba.add_word("告白情书")
jieba.add_word("可爱萝莉")
jieba.add_word("浪漫玫瑰")
jieba.add_word("绚丽烟花")
jieba.add_word("兰博基尼")
jieba.add_word("豪华邮轮")
jieba.add_word("一生一世")
jieba.add_word("豪华飞机")
jieba.add_word("丘比特之箭")
jieba.add_word("花好月圆")
jieba.add_word("冬季恋歌")

for word in words:
    if len(word)==1:
        continue

for word in words:
    if len(word) == 1:  # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())  # 将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序

for i in range(15):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))


#转成excel
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = file.add_sheet('data')


i=0
for line in words:
    giftname = line.strip('\n')
    sheet.write(i,0,giftname)#行，列，值
    i = i + 1
file.save(excelname)
