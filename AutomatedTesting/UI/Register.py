import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
import random
import sys

sys.path.append(r'D:\python\AutomatedTesting\testCase')
import testNum

testNum.loginnew()

# 请求信息
URL = 'http://192.168.183.129/phpwind/'
browser = webdriver.Chrome()
'''登录'''


class ui(object):
    def __init__(self):

    def register(url):
        print(url)
        '''登录url'''
        newUrl = url + 'index.php'
        browser.get(newUrl)
        browser.find_element_by_id('nav_pwuser').send_keys('admin')
        time.sleep(1)
        browser.find_element_by_id('showpwd').send_keys('admin')
        browser.find_element_by_name('head_login').click()


'''发帖'''


    def Post():
        # print(browser.page_source)
        id = re.findall('<h2 class="forumT"><a href="(.*?)"', browser.page_source)
        '''随机取页面上的模块ID'''
        num = random.randint(0, (len(id)) - 1)
        '''拼接url,跳转到相应的模块'''
        newUrl = URL + id[num]
        print(newUrl)
        browser.get(newUrl)
        '''跳转到发帖页面'''
        browser.find_element_by_id('td_post').click()
        browser.find_element_by_id('atc_title').send_keys('newtiezhi')
        '''切到iFrame中'''
        browser.switch_to.frame('note_iframe')
        browser.find_element_by_xpath('/html/body').send_keys('dfawejfidjfka lj dksf alf dkls adfjl')
        '''跳出iFrame'''
        browser.switch_to.default_content()
        browser.find_element_by_name('Submit').click()
        '''提交后文本内容check'''
        checkSubmit = re.findall('newtiezhi', browser.page_source)
        if (len(checkSubmit) > 0):
            print('提交成功')
        time.sleep(5)


register(URL)
Post()
browser.close()
