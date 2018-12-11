'''
Created on 2018年12月11日

@author: pyli
一个接口，提供分词，词性标注，命名体识别等功能
'''
from configure import environment
import urllib   #用于对URL进行编解码  
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class TestHTTPHandle(BaseHTTPRequestHandler):
    
    def sendBack(self, result):
        resultData = json.dumps({"code": 200}).encode('utf-8')
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(resultData)
    def do_POST(self):
        #接收数据
        inputData = self.rfile.read(int(self.headers['content-length']))
        #解析任务列表
        #获取任务所需结果
        result = {"code": 200}
        #发送计算结果
        self.sendBack(result)
 


def startServer():
    server = HTTPServer((environment.localIP, environment.localPort), TestHTTPHandle)
    server.serve_forever()
    
if __name__ == '__main__':
    startServer()
    
    
    