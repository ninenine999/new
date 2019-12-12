from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome()
browser.get('http://www.baidu.com')
m=browser.find_element(By.CLASS_NAME,'s_ipt')
m.send_keys('select')
print(m)
time.sleep(1)
# m.send_keys(Keys.RETURN)#发送链接值提交
browser.find_element(By.ID,'su').submit()
# print(click.tag_name)
# actions = ActionChains(browser)
# actions.click(click)
time.sleep(1)
browser.close()