# 用来练习selenium和iframe框架
'''
通过selenium来进行QQ空间的登录
QQ空间：
https://qzone.qq.com/

iframe框架：
//*[@id="login_div"]/comment()
账号密码登录按钮：
//*[@id="switcher_plogin"]

账号：
//*[@id="u"]
密码：
//*[@id="p"]
登录按钮：
//*[@id="login_button"]
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://qzone.qq.com/'
# 使用selenium获取url
driver = webdriver.Edge()
driver.get(url)

# 定位iframe标签
iframe = driver.find_element(By.XPATH, '//*[@id="login_frame"]')
# 切换进入标签
driver.switch_to.frame(iframe)

# 点击“账号密码登录”按钮
a = driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]')
a.click()

# 定位账号、密码，点击登录
u = driver.find_element(By.XPATH, '//*[@id="u"]')
u.send_keys('@qq.com')
time.sleep(1)
p = driver.find_element(By.XPATH, '//*[@id="p"]')
p.send_keys('password')
time.sleep(1)
# 点击登录
logion = driver.find_element(By.XPATH, '//*[@id="login_button"]')
logion.click()
time.sleep(3)

driver.quit()

