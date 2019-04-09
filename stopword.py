def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='latin-1').readlines()]
    return stopwords

def movestopwords(sentence):
    stopwords = stopwordslist('stopwords.txt')
    outstr = ''
    for word in sentence:
        if word not in stopwords:
            if word != '\t'and'\n':
                outstr += word
    return outstr