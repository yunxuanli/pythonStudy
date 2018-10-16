# -*- coding: utf-8 -*-
'''
	功能：利用 python 的 urllib 和 BeautifulSoup 包编写网络爬虫，
		  并利用该爬虫爬取网址 《[习近平总书记在上海工作期间对推动
		  “三农”发展的思考与实践](http://www.chinanews.com/gn/2018/10-16/8651068.shtml)》
		  文本内容
	参考网址：
		爬虫函数介绍：https://blog.csdn.net/c406495762/article/details/60137956
		代理 ip 网址：http://www.xicidaili.com/
'''
from urllib import request, parse
import time
from bs4 import BeautifulSoup
import random

# 代理IP
proxy_list = [
    {'http': "120.77.247.147:80"},
    {'http': "183.66.229.214:36121"},
    {'http': "27.22.104.28:30533"},
    {'http': "121.232.148.202:9000"},
    {'http': "183.129.244.16:12471"},
    {'http': "182.100.100.236:9000"},
    {'http': "211.143.241.69:37086"},
    {'http': "180.118.134.201:9000"},
    {'http': "139.196.137.255:8118"},
    {'http': "163.125.249.201:8118"},
    {'http': "120.77.247.147:80"},
    {'http': "183.129.244.16:10367"},
    {'http': "121.232.199.99:9000"},
    {'http': "117.85.217.229:8118"},
    {'http': "117.90.7.182:9000"},
    {'http': "119.145.136.126:8888"},
]

status = False			# 判断是否爬取成功

while not status:
	# 随机抽取一个代理 ip
	proxy = random.choice(proxy_list)
	print(f"ip:{proxy}")
	#创建ProxyHandler
	proxy_support = request.ProxyHandler(proxy)
	#创建Opener
	opener = request.build_opener(proxy_support)
	#添加User Angent
	opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
	#安装OPener
	request.install_opener(opener)
	html =""
	try:
	    html = request.urlopen("http://www.chinanews.com/gn/2018/10-16/8651068.shtml")
	except Exception as e:
	    print(e)

	print(html)
	if html != "":	
		#print(html)
		bsObj = BeautifulSoup(html, "html.parser")
		print("OK")

		news = bsObj.findAll("div",{"class":"left_zw"})[0].get_text()
		print(f"news{news}")

		fnews = open('data/news.txt', 'w', encoding="utf-8")

		fnews.write(news)
		status = True
	else:
		print("ERROR!")