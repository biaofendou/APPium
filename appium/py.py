# coding=utf-8

from appium import webdriver

desired_caps = {

    'platformName': 'Android',

    'deviceName': '127.0.0.1:62001',

    'platformVersion': '5.1.1',

    # apk包名

    'appPackage': 'com.android.settings',

    # apk的launcherActivity

    'appActivity': 'Settings'

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print(desired_caps)
driver.find_element_by_id("com.android.settings:id/search").click()
driver.find_element_by_id("com.android.settings:id/search").send_keys('hello')
driver.quit()
