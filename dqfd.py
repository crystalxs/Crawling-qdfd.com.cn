__author__ = 'Crystal'

import re
import requests  # 导入requests模块
from bs4 import BeautifulSoup  # 从bs4包中导入BeautifulSoup模块
import time
import datetime


# 设置请求头
# 更换一下爬虫的User-Agent，这是最常规的爬虫设置
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}  

# 需要爬取的网址
url = 'http://www.qdfd.com.cn/qdweb/realweb/indexnew.jsp'

# 发送请求，获取的一个Response对象
web_data = requests.get(url, headers=headers)

# 设置web_data.text会采用web_data.encoding指定的编码，一般情况下不需要设置，requests会自动推断
# 鉴于大神帮忙检测网上房地产编码采用gb2312
web_data.encoding = 'gb2312'
# 得到网页源代码
content = web_data.text

# 使用lxml解析器来创建Soup对象
soup = BeautifulSoup(content, 'lxml')

table_area_0 = soup.select('div.con2l.r div.con2lx.mg2.xi12 tr.cu td')
n0 = len(table_area_0)
table_area_1 = soup.select('div.con2l.r div.con2lx.mg2.xi12 tr.bghui td')
n1 = len(table_area_1)
table_area_2 = soup.select('div.con2l.r div.con2lx.mg2.xi12 tr td')
n2 = len(table_area_2)

f = open('C:\\Users\\Administrator\\Desktop\\output.txt','a',encoding='gb2312')
print('{0}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
print('{0},{1},{2},{3},{4},{5}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),table_area_0[5].text,table_area_0[6].text,table_area_0[7].text,table_area_0[8].text,table_area_0[9].text),file=f)
for i in range(n1//5):
    print('{0},{1},{2},{3},{4},{5}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),table_area_1[5*i].text,table_area_1[5*i+1].text,table_area_1[5*i+2].text,table_area_1[5*i+3].text,table_area_1[5*i+4].text),file=f)
    n = i+3+i
    print('{0},{1},{2},{3},{4},{5}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),table_area_2[5*n].text,table_area_2[5*n+1].text,table_area_2[5*n+2].text,table_area_2[5*n+3].text,table_area_2[5*n+4].text),file=f)
f.close()