from src.nlpTool.contentClean import cleanArticle
from src.nlpTool.paragraphSplit import splitTextIntoParagraphList
from src.nlpTool.sentenceSplit import splitTextIntoSentences
from src.nlpTool.wordSegment import splitSentenceIntoWords
from src.entity.article import Article
import time
if __name__ == '__main__':
    article = Article()
    article.title = "题目"
    article.content = """我爱中国。
    这是我的祖国。
    
    我出生在这里。也在这里长大。"""
    t1 = time.time()
    cleanArticle(article)
    splitTextIntoParagraphList(article)
    splitTextIntoSentences(article)
    splitSentenceIntoWords(article)
    t2 = time.time()
    print(t2-t1)
    print(article.__dict__)
