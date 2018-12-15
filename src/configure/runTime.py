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


#任务和需要执行的函数名的对应表
TASK_METHOD_MAP = {
    'paragraphSplit': 'splitTextIntoParagraphList',
    'sentenceSplit': 'splitTextIntoSentences',
    'wordSegment': 'splitSentenceIntoWords'
}

#任务和article的属性对应表
TASK_ARTICLE_ATTR_MAP = {
    'paragraphSplit': 'paragraphList',
    'sentenceSplit': 'sentencesList',
    'wordSegment': 'words'
}