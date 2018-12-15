'''
Created on 2018年12月12日

@author: pyli
'''
from src.configure import runTime

#递归的从任务依赖表中查询当前任务名称对应的前序任务
def findAllEarlierTask(taskName, res):
    if runTime.TASK_DEPEND_MAP[taskName]==[]:
        return res
    else:
        for name in runTime.TASK_DEPEND_MAP[taskName]:
            res.append(name)
            findAllEarlierTask(name, res)
        return res
    
#获取任务列表的所有前序任务，保证是从最后到最前的顺序
def getNecessaryTaskList(taskList):
    necessaryTaskList = []
    for taskName in taskList:
        if taskName not in necessaryTaskList:
            necessaryTaskList.append(taskName)
        earlierTaskList = findAllEarlierTask(taskName, [])
        if earlierTaskList!=None:
            for necessaryTsakNeme in earlierTaskList:
                if necessaryTsakNeme not in necessaryTaskList:
                    necessaryTaskList.append(necessaryTsakNeme)
    necessaryTaskList.reverse()
    return necessaryTaskList

def getTaskList(articleList, url):
    for article in articleList:
        article.taskList = url[1:].split('-')
        article.mustTaskList = getNecessaryTaskList(article.taskList)
        print("调用方式是", url)
    return articleList

if __name__ == '__main__':
    res = getNecessaryTaskList(['wordSegment'])
    print(res)
    
    
    