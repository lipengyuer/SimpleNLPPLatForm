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
from src.configure import tools
import time
localIP = tools.get_host_ip()
localPort = 1024
restfulUrl = 'http://' + localIP +':' + str(localPort) + '/sentenceSplit'
restfulUrl = 'http://' + localIP +':' + str(localPort) + '/wordSegment-sentenceSplit'

fileName = r'E:\Data4Huang.txt'
# with open(fileName, 'r', encoding='utf8') as f:
with open(fileName, 'r') as f:

    line = f.readline()
    line = line.split('kabukabu')[4]
    count = 0
    tCost = 0.
    dataBatch = []
    while line!=None:
        content ={'title':'','content':line}
        # print(content)
        dataBatch.append(content)
        if len(dataBatch)==1000:
            data = json.dumps(dataBatch)
            headers = {"Content-Type": "application/json"}
            t1 = time.time()
            resp = requests.post(restfulUrl, headers=headers, data=data.encode('utf-8'))
            t2 = time.time()
            tCost += t2-t1
            print(json.loads(resp.text))
            print(count, tCost, tCost / count)
            dataBatch = []

        try:
            line = f.readline()
            line = line.split('kabukabu')[4]
            count += 1
        except:
            pass



