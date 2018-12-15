'''
Created on 2018年12月11日

@author: pyli
'''
from pyhanlp import HanLP
CRFnewSegment = HanLP.newSegment("crf")
def splitSentenceIntoWords(article):
    article.words = []
    for sentences in article.sentencesList:
        for sentence in sentences:
            words = CRFnewSegment.seg(sentence)
            words = list(map(lambda x:str(x), words))
            # print("分词结果是", words)
            article.words += words