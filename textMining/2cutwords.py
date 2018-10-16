# -*- coding: utf-8 -*-
'''
	功能：利用 python 的 jeiba 分词包对所爬取的数据进行分词、词性标注
	参考网址：
		jieba 分词 github：https://github.com/fxsjy/jieba
'''
import jieba
from os import path

jieba.load_userdict("userdict.txt")		# 用户自定义词典

d = ""
stopwords_path = "stop_words.txt" 		# 停用词词表

text_path = 'news.txt' 					#设置要分析的文本路径
text = open(path.join(d, text_path),'r', encoding='UTF-8').read()

# 功能：停用词词典加载
def stopWordProcess():
	'''
		功能：停用词词典加载
		input:
			
		output:
			f_stop_seg_list	list 	停用词词典列表
	'''
	f_stop = open(stopwords_path,'r', encoding='UTF-8')
	try:
	    f_stop_text = f_stop.read()
	finally:
	    f_stop.close( )
	f_stop_seg_list=f_stop_text.split('\n')
	return f_stop_seg_list

# 功能：结巴分词
def jiebaclearText(text):
	'''
		功能：分词并过滤停用词后的数据
		input:
			text 	String	文本内容
		output:
			''.join(mywordlist)	String	分词并过滤停用词后的数据
	'''
	mywordlist = []
	seg_list = jieba.cut(text, cut_all=False)
	liststr="/ ".join(seg_list)
    
	f_stop_seg_list= stopWordProcess()			# 停用词词典加载

	for myword in liststr.split('/'):
	    if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
	        mywordlist.append(myword)
	return ''.join(mywordlist)

text = jiebaclearText(text)
print(text)


import jieba.posseg as pseg
# 功能：分词并过滤停用词后进行词性标注的数据
def jiebaclearPosText(text):
	'''
		功能：分词并过滤停用词后进行词性标注的数据
		input:
			text 	String	文本内容
		output:
			''.join(mywordlist)	String	分词并过滤停用词后的数据
	'''
	mywordlist = []
	seg_list = pseg.cut(text)

	f_stop_seg_list= stopWordProcess()			# 停用词词典加载

	for word, flag in seg_list:
	    if not(word.strip() in f_stop_seg_list) and len(word.strip())>1:
	        mywordlist.append(word+"/"+flag+"\n")

	with open('word_posseg.txt', 'w',encoding = "utf-8") as f_word_posseg:
		f_word_posseg.write(''.join(mywordlist))

	return ''.join(mywordlist)

pos_text = jiebaclearPosText(text)
print(pos_text)



