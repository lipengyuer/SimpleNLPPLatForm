'''
Created on 2018年12月11日

@author: pyli
'''
from configure import tools

localIP = tools.get_host_ip()
localPort = 1024
print("本机IP是", localIP)