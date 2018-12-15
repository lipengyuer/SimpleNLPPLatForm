from src.configure import environment, runTime
from src.nlpTool.paragraphSplit import splitTextIntoParagraphList
from src.nlpTool.sentenceSplit import splitTextIntoSentences
from src.nlpTool.wordSegment import splitSentenceIntoWords

#执行必需任务列表中的每一项任务
def processArticle(articleList):
    # article.words = []
    # article.sentencesList = []
    # article.paragraphList = []
    for article in articleList:
        print("请求的任务是", article.taskList)
        print("必需的任务是",article.mustTaskList )
        for task in article.mustTaskList:
            print("当前执行的任务是", task)
            globals().get(runTime.TASK_METHOD_MAP[task])(article)
