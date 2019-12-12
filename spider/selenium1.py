from selenium import webdriver
from selenium.webdriver.common.by import By#引入查找的by语句
import time
browser=webdriver.Chrome()
# browser=webdriver.PhantomJS()???
browser.get('http://www.baidu.com')

# print(browser.page_source)
# browser.close()
# input_first=browser.find_element_by_id('wrapper_wrapper')
input_first=browser.find_element(By.CLASS_NAME, 's_ipt')
input_first.send_keys('selenuim')
time.sleep(1)
input_first.clear()
time.sleep(1)
input_first.send_keys('select')
time.sleep(1)
print(input_first)
browser.close()
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()
#