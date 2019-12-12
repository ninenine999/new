from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
bowser=webdriver.Chrome()
# bowser.maximize_window()
bowser.get('http://mail.163.com')
time.sleep(3)#没有加时间时不能成功，原因应该是网页没有加载完
bowser.switch_to.frame("x-URS-iframe")
userName=bowser.find_element(By.NAME,'email')
userName.clear()
userName.send_keys('wymdyw@163.com')
time.sleep(1)
userPassword=bowser.find_element(By.NAME,'password')
userPassword.clear()
time.sleep(1)
userPassword.send_keys('wgjdyw.416110')
bowser.find_element(By.ID,'dologin').click()
time.sleep(1)
