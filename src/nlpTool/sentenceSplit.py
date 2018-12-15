'''
Created on 2018年12月11日

@author: pyli
'''
#将文章各个段落切分成句子，便于分词
def splitTextIntoSentences(article):
    article.sentencesList = []
    for paragraph in article.paragraphList:
        tempRes = []
        sentences = paragraph.split("。")
        for sentence in sentences:
            if sentence!="":
                tempRes.append(sentence + "。")
        article.sentencesList.append(tempRes)

