def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords

def movestopwords(sentence):
    stopwords = stopwordslist('stopwords.txt')
    outstr = ''
    for word in sentence:
        if word not in stopwords[0]:
            if word != '\t'and'\n':
                outstr += word
    return outstr