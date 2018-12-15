from src.entity.article import Article
from src.configure import environment, runTime
import json

def orgnizeJson2ArticleList(jsonStrs):
    jsonDataList = json.loads(jsonStrs.decode('utf8'))
    articleList = []
    for jsonData in jsonDataList:
        article = Article()
        article.title = jsonData.get('title', '')
        article.content = jsonData.get('content', '')
        articleList.append(article)
    return articleList

def orgnizeArticleList2Json(articleList):
    resultMapList = []
    for article in articleList:
        resultMap = {}
        for task in article.taskList:
            resultMap[task] = getattr(article, runTime.TASK_ARTICLE_ATTR_MAP[task])
        resultMapList.append(resultMap)
    return resultMapList
