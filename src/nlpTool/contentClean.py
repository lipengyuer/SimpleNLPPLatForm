'''
Created on 2018年12月11日

@author: pyli
'''
import re

#对文本进行预处理
def cleanArticle(article):
    article.title = filterHtmlTag(article.title)
    article.title = strQ2B(article.title)
    article.content = filterHtmlTag(article.content)
    article.content = strQ2B(article.content)

#https://blog.csdn.net/yangyang_1009/article/details/19168055?utm_source=tuicool

def filterHtmlTag(htmlStr):
    '''
    过滤html中的标签
    :param htmlStr:html字符串 或是网页源码
    '''
    #先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlStr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('\n',s)#将br转换为换行
    blank_line=re.compile('\n+')#去掉多余的空行
    s = blank_line.sub('\n',s)
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    s=replaceCharEntity(s)#替换实体
    return s


def replaceCharEntity(htmlStr):
    '''
    替换html中常用的字符实体
    使用正常的字符替换html中特殊的字符实体
    可以添加新的字符实体到CHAR_ENTITIES 中
CHAR_ENTITIES是一个字典前面是特殊字符实体  后面是其对应的正常字符
    :param htmlStr:
    '''
    CHAR_ENTITIES={'nbsp':' ','160':' ',
            'lt':'<','60':'<',
            'gt':'>','62':'>',
            'amp':'&','38':'&',
            'quot':'"','34':'"',}
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlStr)
    while sz:
        entity=sz.group()#entity全称，如>
        key=sz.group('name')#去除&;后的字符如（" "--->key = "nbsp"）    去除&;后entity,如>为gt
        try:
            htmlStr= re_charEntity.sub(CHAR_ENTITIES[key],htmlStr,1)
            sz=re_charEntity.search(htmlStr)
        except KeyError:
            #以空串代替
            htmlStr=re_charEntity.sub('',htmlStr,1)
            sz=re_charEntity.search(htmlStr)
    return htmlStr

#全角转半角
def strQ2B(ustring):
    ss = ''
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            rstring += chr(inside_code)
        ss += rstring
    return ss

if __name__ == '__main__':
    s = "我是中国人244。.,/。，。啊sfdfs..。"
    print(s)
    print(strQ2B(s))
    s = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <link rel="canonical" href="https://blog.csdn.net/yangyang_1009/article/details/19168055"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit"/>
    <meta name="force-rendering" content="webkit"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="referrer" content="always">
    <meta http-equiv="Cache-Control" content="no-siteapp" /><link rel="alternate" media="handheld" href="#" />
    <meta name="shenma-site-verification" content="5a59773ab8077d4a62bf469ab966a63b_1497598848">
        <meta name="csdn-baidu-search" = content='{"autorun":true,"install":true,"keyword":"python+%E5%8E%BB%E9%99%A4+style"}'>
        <script src="https://csdnimg.cn/release/phoenix/vendor/tingyun/tingyun-rum-blog.js"></script>

    <link href="https://csdnimg.cn/public/favicon.ico" rel="SHORTCUT ICON">
    <title>python 去除html标签的几种方法 - 阳阳的专栏 - CSDN博客</title>
"""
    print(filterHtmlTag(s))