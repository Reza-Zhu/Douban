from bs4 import BeautifulSoup
import requests
import re
import jieba
import wordcloud
from count import Count
from stopword import movestopwords
import os
num=0

if not os.path.exists('.\comment.txt'):
    for nums in range(10):
        URL='https://movie.douban.com/subject/1291546/comments?start=%s&limit=20&sort=time&status=P'%num
        html=requests.get(URL).text
        soup=BeautifulSoup(html,'lxml')
        img_ul=soup.find_all('span',{'class':'short'})
        num=num+20
        for cm in img_ul:
            pattern_description = re.compile('<span class="short">([\s\S]+)</span>')
            list_description = re.findall(pattern_description,str(cm))

            with open('comment.txt','a',encoding='utf-8') as f:
                f.write(list_description[0])
                f.close()
txt=open('comment.txt',encoding='utf-8').read()
res=movestopwords(txt)
w=wordcloud.WordCloud(width=1000,font_path='C:\Windows\Fonts\msyh.ttf',height=700)
listword=jieba.lcut(res)
w.generate(" ".join(listword))
w.to_file("new.png")
Count('comment.txt','的','也','太')