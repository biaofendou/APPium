# -*- coding:utf8 -*-
from urllib import request
from urllib import parse
from urllib.request import urlopen
from API.login_user import login_user


def doctor_list(current, size):
    url = "http://106.13.91.109:1234/mo/user/list"
    print(login_user("admin", "MTIzNDU2"))
    # 定义请求数据并赋值
    data = {}
    data['current'] = str(current)
    data['size'] = str(size)
    data = parse.urlencode(data)
    # 将数据和url进行连接
    requests = url + '?' + data
    header = {
        "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJib2R5Ijoie1wibmFtZVwiOlwi5rWLOFwiLFwicGVybWlzc2lvblwiOlwiVVNFUlwiLFwidXNlcklkXCI6XCI3M2M0NWJlN2U4NTc0YmIzYjQxOWYwYzJjMzZmMTcwMFwiLFwidXNlcm5hbWVcIjpcInVzZXJcIn0iLCJleHAiOjE1NTg3NjA3Mjd9.tBH-rXwPEThiZdhBMFNWaDWaAZMhvpJfbcY4dyVNVLfg1tUQSSlOze9Cqq2jHk8At-fGy3euaFZJtVRFmNIMjg"
    }
    requestss = request.Request(url=requests, headers=header)
    # 打开请求获取对象
    requestResponse = urlopen(requestss)
    # 读取服务端返回的对象
    responseStr = requestResponse.read()
    # 打印数据
    ResponseStr = responseStr.decode("utf-8")
    print(ResponseStr)
doctor_list(1, 10)