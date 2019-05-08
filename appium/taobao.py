# coding=utf-8

from appium import webdriver
import time

desired_caps = {

    'platformName': 'Android',

    'deviceName': '127.0.0.1:62001',

    'platformVersion': '5.1.1',

    # apk包名

    'appPackage': 'com.taobao.taobao',

    # apk的launcherActivity

    'appActivity': 'com.taobao.tao.welcome.Welcome',

    # unicodeKeyboard是使用unicode编码方式发送字符串
    'unicodeKeyboard': True,

    #resetKeyboard是将键盘隐藏起来
    'resetKeyboard': True

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠5秒等待页面加载
time.sleep(5)
driver.find_element_by_id("	com.taobao.taobao:id/yes").click()
time.sleep(5)
driver.find_element_by_id("	com.taobao.taobao:id/home_searchedit").click()
driver.find_element_by_id("	com.taobao.taobao:id/search/Edit").click()
driver.find_element_by_id("	com.taobao.taobao:id/search/Edit").send_keys(u'男装')
driver.quit()
