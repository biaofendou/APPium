# -*- coding:utf-8 -*-
import os
import time
import csv


# App类
class APP(object):
    def __init__(self):
        self.content = ''
        self.startTime = 0

    # 启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.maiyang/.MainActivity'
        self.content = os.popen(cmd)

    # 停止App
    def StopApp(self):
        #cmd = 'adb shell am force-stop com.maiyang'
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    # 获取启动时间
    def GetLaunchTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


class Controller(object):
    def __init__(self, count):
        self.app = APP()
        # time.sleep(5)
        self.counter = count
        time.sleep(3)
        self.alldata = [('timestammp', 'elapsedtime')]

    # 单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        elapsedtime = self.app.GetLaunchTime()
        self.app.StopApp()
        currentTime = self.getCurrentTime()
        self.alldata.append((currentTime, elapsedtime))

    # 多次测试
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter -= 1

    # 获取当前时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据存储
    def SaveDataToCSV(self):
        with open('E:\Python_workspace\PythonProgram\maiyang\launchTime\\runtime.csv', 'w') as file:
            writer = csv.writer(file,dialect='excel')
            writer.writerows(self.alldata)


if __name__ == '__main__':
    controller = Controller(1)
    controller.run()
    controller.SaveDataToCSV()


