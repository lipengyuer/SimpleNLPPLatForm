'''
Created on 2018年12月11日

@author: pyli
'''
#提供的服务名称列表
AVAILABLE_TASK_LIST = ['wordSegment', 'sentenceSplit', 'paragraphSplit', 'posTag' 'nerDetect']
#任务依赖表
TASK_DEPEND_MAP = {
    'paragraphSplit': [],
    'sentenceSplit': ['paragraphSplit'],
    'wordSegment': ['sentenceSplit']
    }