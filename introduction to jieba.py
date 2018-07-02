# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 18:47:55 2018

@author: beatr
"""

import jieba
#分词
testSentence='利用python进行数据分析'
print('1.精确模式分词结果:'+'/'.join(jieba.cut(testSentence,cut_all=False)))
print('1.全模式分词结果:'+'/'.join(jieba.cut(testSentence,cut_all=True)))
print('3.搜索引擎模式分词结果'+'/'.join(jieba.cut_for_search(testSentence)))
print('1.默认（精确模式）分词结果:'+'/'.join(jieba.cut(testSentence)))
#查看词性
import jieba.posseg
words=jieba.posseg.cut(testSentence)
for item in words:
    print(item.word+'----'+item.flag)
    
    
#词典加载
testSentence2='简书书院是一个很好的交流平台'
print('+----------+---------+-------+--------+---------')
print('1.加载词典前分词结果：')
print([item for item in jieba.posseg.cut(testSentence2)])
print('+----------+---------+-------+--------+---------')
jieba.load_userdict('D:\\anaconda\\Lib\\site-packages\\jieba\\dict21.txt')
print('2.加载词典后分词结果：')
print([item for item in jieba.posseg.cut(testSentence2)])
#调整词典
#调高词频
testSentence3='数据分析与数据挖掘'
print('1.原始分词结果：'+'/'.join(jieba.cut(testSentence3,HMM=False)))
jieba.add_word('的应用')
print('2.使用add_word(word,freq=None,tag=None)结果：'+'/'.join(jieba.cut(testSentence3,HMM=False)))
jieba.suggest_freq('的应用',tune=True)
print('3.使用suggest_freq(segment,tune=True)结果：'+'/'.join(jieba.cut(testSentence3,HMM=False)))
#降低词频

jieba.suggest_freq(('中','将'),True)
print('使用suggest_freq(("segmentPart1","segmentPart2"),True)分词结果：'
      +'/'.join(jieba.cut('在简书中将尽力呈现优质内容',HMM=False)))

#返回词语所在位置
import jieba.analyse
print('1.精确模式分词结果:')
print([item for item in jieba.tokenize('数据分析与数据挖掘的应用')])
print('--------------')
print('2.采取搜索模式结果：')
print([item for item in jieba.tokenize('数据分析与数据挖掘的应用',mode='search')])

#提取文本中的关键词
import jieba.analyse
print(jieba.analyse.extract_tags('我喜欢广州小蛮腰',3))
print(jieba.analyse.extract_tags('我喜欢广州广州小蛮腰',3))
print(jieba.analyse.extract_tags('我喜欢广州广州广州小蛮腰',3))
#其结果是结合文中出现的词频与字典中的词频进行排序。




