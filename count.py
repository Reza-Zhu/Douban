import jieba
def Count(txt,str1,str2,str3):
    txt=open('%s'%txt,'rb').read()
    words=jieba.lcut(txt)
    count1=count2=count3=0
    for word in words:
        if word=='%s'%str1:
            count1=count1+1
        elif word=='%s'%str2:
            count2=count2+1
        elif word=='%s'%str3:
            count3=count3+1
    print('\'%s\'出现%d次'%(str1,count1))
    print('\'%s\'出现%d次'%(str2,count2))
    print('\'%s\'出现%d次'%(str3,count3))