'''
Created on 2018年12月11日

@author: pyli
一个接口，提供分词，词性标注，命名体识别等功能
'''
import os, sys
path = os.getcwd()
sys.path.append(os.path.dirname(path))
from src.configure import environment, runTime
import urllib   #用于对URL进行编解码  
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.system.task import getTaskList
from src.entity.orgnizeData import orgnizeJson2ArticleList, orgnizeArticleList2Json
from src.system.worker import processArticle
class TestHTTPHandle(BaseHTTPRequestHandler):
    
    def sendBack(self, result):
        resultData = json.dumps(result).encode('utf-8')
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(resultData)
    def do_POST(self):
        #接收数据
        inputData = self.rfile.read(int(self.headers['content-length']))
        articleList = orgnizeJson2ArticleList(inputData)
        #解析任务列表
        articleList = getTaskList(articleList, self.path)
        processArticle(articleList)
        resultMapList = orgnizeArticleList2Json(articleList)
        #获取任务所需结果
        #发送计算结果
        self.sendBack(resultMapList)
 


def startServer():
    server = HTTPServer((environment.localIP, environment.localPort), TestHTTPHandle)
    server.serve_forever()
    
if __name__ == '__main__':
    startServer()
    
    
    