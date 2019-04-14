from bs4 import BeautifulSoup
import requests
import re
import jieba
import wordcloud
from count import Count
from stopword import movestopwords
import os,time
num=0
header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Connection':'keep-alive',
'Cookie':'ll="118172"; bid=RL-Ud9-M8Is; __utmc=30149280; __utmc=223695111; __yadk_uid=1zmMhETBDMVis3yMbUOGhNAuDNXvCMfO; _vwo_uuid_v2=D028E2287D9969D2E76DEC3EB4593E4C6|6481f784be57b1e49c6e37458118f7ae; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18489; douban-profile-remind=1; dbcl2="184896369:3JzWAGgS7TY"; ck=76wX; __utma=30149280.1020408546.1555117224.1555117412.1555124605.3; __utmz=30149280.1555124605.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utmb=30149280.8.10.1555124605; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1555125272%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fcat%3D1002%26q%3D%25E9%259C%25B8%25E7%258E%258B%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.690157687.1555117412.1555117412.1555125272.2; __utmb=223695111.0.10.1555125272; __utmz=223695111.1555125272.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_id.100001.4cf6=48856d09d3a72324.1555117412.2.1555125277.1555117413',
'Referer':'https://movie.douban.com/subject/1291546/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


if not os.path.exists('.\comment.txt'):
    for nums in range(20):
        URL='https://movie.douban.com/subject/1291546/comments?start=%s&limit=20&sort=new_score&status=P'%num
        html=requests.get(URL,headers=header).text
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
print(time.clock())#12.3s