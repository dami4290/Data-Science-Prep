multidict={
    'firstlevel': {
        'secondlevel': {
            'thirdlevel':'I am here'
        }
    }
}
multidict["newlevel"]={"newlevel2":"dfsjlk"}
print(multidict)
def frequencyCounter(corpus):
    wordfrequency=dict()
    for document in corpus:
        words=document.split()
        for word in words:
            if word not in wordfrequency:
                wordfrequency[word]={'totalcount':1, 'documents': {document:1}}
            else:
                wordfrequency[word]['totalcount']+=1
                if document in wordfrequency[word]['documents']:
                    wordfrequency[word]['documents'][document]+=1
                else:
                    wordfrequency[word]['documents'][document]=1
    return wordfrequency
corpus = [
    "This is the multidimensional dictionary.",
    "This dictionary stores the sub dictionary.",
    "And this is the third containing the word and count.",
    "Is this the first level of dictionary?"]
a=frequencyCounter(corpus)
print(a)
