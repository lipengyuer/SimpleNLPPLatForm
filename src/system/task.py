'''
Created on 2018年12月12日

@author: pyli
'''
from configure import runTime

def findAllEarlierTask(taskName, res):
    if runTime.TASK_DEPEND_MAP[taskName]==[]:
        return res
    else:
        for name in runTime.TASK_DEPEND_MAP[taskName]:
            res.append(name)
            findAllEarlierTask(name, res)
        return res
            
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
    print(necessaryTaskList)
    
if __name__ == '__main__':
    getNecessaryTaskList(['wordSegment'])
    
    
    