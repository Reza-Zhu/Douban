from bs4 import BeautifulSoup
import requests
import re
import jieba
import wordcloud
from count import Count
from stopword import movestopwords
num=0
for nums in range(10):
    URL='https://movie.douban.com/subject/1291546/comments?start=%s&limit=20&sort=time&status=P'%num
    html=requests.get(URL).text
    soup=BeautifulSoup(html,'lxml')
    img_ul=soup.find_all('span',{'class':'short'})
    num=num+20
    for cm in img_ul:
        pattern_description = re.compile('<span class="short">([\s\S]+)</span>')
        list_description = re.findall(pattern_description,str(cm))
        #print(list_description)
        with open('comment2.txt','a',encoding='utf-8') as f:
            f.write(list_description[0])
            f.close()
txt=open('comment2.txt',encoding='utf-8').read()
w=wordcloud.WordCloud(width=1000,font_path='C:\Windows\Fonts\msyh.ttf',height=700)
listword=jieba.lcut(txt)
#print(listword)

result=movestopwords(listword)
#print(result)

w.generate(" ".join(jieba.lcut(result)))
w.to_file("new.png")
Count('comment1.txt','的','也','太')