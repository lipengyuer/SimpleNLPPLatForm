# encoding:utf8
'''
Created on Oct 11, 2016

@author: foxbat
'''
import sys
import os
path = os.getcwd()
path = os.path.dirname(path)
sys.path.append(path)

import json
import requests
import time
#keyExpression
from configure import tools
localIP = tools.get_host_ip()
localPort = 1024
restfulUrl = 'http://' + localIP +':' + str(localPort)
content =[{'title':'','content':'''
我明天要去苏州博物馆了,玩解谜游戏.
''' }]

data = json.dumps(content)
headers = {"Content-Type": "application/json"}
resp = requests.post(restfulUrl, headers=headers, data=data.encode('utf-8'))

print(json.loads(resp.text))


