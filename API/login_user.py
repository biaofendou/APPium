# -*- coding:utf-8 -*-
from urllib import request
import json

def login_user(user,password):
    url = "http://106.13.91.109:1234/mo/login/common"
    data = {}
    data["username"] = user
    data["password"] = password
    header = {}
    header["Content-Type"] = "application/json"
    # 数据编码以及赋值
    json_data = json.dumps(data).encode(encoding="utf-8")
    req = request.Request(url=url, data=json_data, headers=header)
    # 打开地址
    ResponseStr = request.urlopen(req)
    # 读取值
    ResponseStr = ResponseStr.read()
    ResponseStr = ResponseStr.decode("utf-8")
    login_data = json.loads(ResponseStr)
    return login_data


