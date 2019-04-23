# coding=utf-8

from appium import webdriver

desired_caps = {

    'platformName': 'Android',

    'deviceName': 'B2T0216323001136',

    'platformVersion': '8.0',

    # apk包名

    'appPackage': 'com.android.calculator2',

    # apk的launcherActivity

    'appActivity': 'com.android.calculator2.Calculator'

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_name('7').click()
driver.find_element_by_name('8').click()
driver.find_element_by_name('+').click()
driver.find_element_by_name('8').click()
driver.find_element_by_name('=').click()
driver.quit()