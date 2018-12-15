'''
Created on 2018年12月11日

@author: pyli
'''
#将文章切分为段落
def splitTextIntoParagraphList(article):
    tempRes = article.content.split('\n')
    article.paragraphList = []
    for line in tempRes:
        line = line.strip()
        if len(line)>0:
            article.paragraphList.append(line)