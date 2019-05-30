from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from PIL import Image
import requests,re,jieba,wordcloud
import tkinter as tk
from stopword import movestopwords
window = tk.Tk()
window.title('电影热评')
window.geometry('400x200')
e=tk.Entry(window,show=None,width=15)
e.place(x=150,y=20)
num=0
header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Connection':'keep-alive',
'Cookie':'ll="118172"; bid=RL-Ud9-M8Is; _vwo_uuid_v2=D028E2287D9969D2E76DEC3EB4593E4C6|6481f784be57b1e49c6e37458118f7ae; __yadk_uid=EkhwpZ57ixkLYp2LEj5zhWDNG98WU0KM; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18489; douban-profile-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1556516424%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DAcLF_WM_Ucfg6xyGCku-hP494LqMUHWK4Yi2_VRXVRm%26wd%3D%26eqid%3D91716c6a00019978000000065cc68e42%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1020408546.1555117224.1556284006.1556516426.10; __utmc=30149280; __utmz=30149280.1556516426.10.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="184896369:3JzWAGgS7TY"; ck=76wX; ap_v=0,6.0; _pk_id.100001.8cb4=2c8641992ff34d68.1555117221.3.1556518200.1555125266.; __utmt=1; __utmb=30149280.5.10.1556516426',
'Referer':'https://movie.douban.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

def insert_point():
    global num,name
    name=e.get()
    # name = input('?')
    num_url='https://movie.douban.com/subject_search?search_text=%s&cat=1002'%name
    driver = webdriver.Chrome()
    driver.get(num_url)
    num_html_2=etree.HTML(driver.page_source)
    num_html_data=num_html_2.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a/@href')
    film=re.compile('[1-9][0-9]{,}')
    film_num=re.findall(film,num_html_data[0])
    print(film_num[0])

    # if not os.path.exists('.\comment.txt'):
    for nums in range(5):
            URL='https://movie.douban.com/subject/{0}/comments?start={1}&limit=20&sort=new_score&status=P'.format(film_num[0],num)
            html=requests.get(URL,headers=header).text
            soup=BeautifulSoup(html,'lxml')
            img_ul=soup.find_all('span',{'class':'short'})
            num=num+20
            for cm in img_ul:
                pattern_description = re.compile('<span class="short">([\s\S]+)</span>')
                list_description = re.findall(pattern_description,str(cm))
                # print(list_description[0])
            with open('%s.txt'%name, 'a', encoding='utf-8') as f:
                f.write(list_description[0])
                f.close()

    txt = open('.\%s.txt'%name, encoding='utf-8').read()
    res = movestopwords(txt)
    w = wordcloud.WordCloud(width=1000, font_path='C:\Windows\Fonts\msyh.ttf', height=700)
    listword = jieba.lcut(res)
    w.generate(" ".join(listword))
    w.to_file("%s.png"%name)
def show():
    global name
    img = Image.open('.\%s.png'%name)
    img.show()
b1=tk.Button(window,text='启动',width=15,
              height=2, command=insert_point).place(x=50,y=50)
b2=tk.Button(window,text='查看词云',width=15,
              height=2, command=show).place(x=200,y=50)
l1=tk.Label(window,text='请输入要查询的电影： ')
l1.place(x=20,y=0)

window.mainloop()

