# -*- coding:utf-8 -*-
import time
from appium import webdriver
import unittest
import warnings


class MyTestCase(unittest.TestCase):
    # 脚本初始化,获取操作实例
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.maiyang'
        desired_caps['appActivity'] = '.MainActivity'
        # desired_caps["unicodeKeyboard"] = "True"
        # desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 释放实例,释放资源
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # def test_something(self):
    #     self.assertEqual(True, True)

    # 测试登录
    def test_Login(self):
        # 获取登录类
        user = self.driver.find_elements_by_class_name("android.widget.EditText")[0]
        user.send_keys("user")
        password = self.driver.find_elements_by_class_name("android.widget.EditText")[1]
        password.send_keys("123456")
        login_button = self.driver.find_elements_by_class_name("android.widget.Button")[0]
        login_button.click()
        try:
            if self.driver.find_elements_by_class_name('new UiSelector().text("报警")')[0].is_displayed():
                exist = True
        except Exception:
            exist = False
        self.assertEqual(exist, True)

    # 查看历史报警
    def test_History(self):
        history_button = self.driver.find_elements_by_class_name("android.widget.Button")[0]
        history_button.click()
        try:
            if self.driver.find_elements_by_android_uiautomator('new UiSelector().text("历史报警")')[0].is_displayed():
                exist = True
        except Exception:
            exist = False
        #  返回
        reback = self.driver.find_elements_by_class_name("android.widget.Button")[0]
        reback.click()
        self.assertEqual(exist, True)

    # 添加病人
    def test_patient(self):
        patient_button = self.driver.find_elements_by_class_name("android.view.View")[1]
        patient_button.click()
        try:
            if self.driver.find_elements_by_android_uiautomator('new UiSelector().text("搜索病人")')[0].is_displayed():
                exist = True
        except Exception:
            exist = False

        self.assertEqual(exist, True)

    # 查找病人
    def test_patientSearch(self):
        search = self.driver.find_elements_by_android_uiautomator('new UiSelector().text("搜索病人")')[0]
        search.send_keys("病人a")
        search_button = self.driver.find_elements_by_class_name("android.widget.Button")[0]
        search_button.click()

    # 查看详情
    # 修改数据


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_Login"))
    suite.addTest(MyTestCase("test_History"))
    suite.addTest(MyTestCase("test_patient"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()  # 运行所有的测试用例
