"""
1. Attempt at a model that finds out the most important words in a given document using
i) term frequency
ii) inverse document frequency.

You may assume the document to be a string.
"""

from textblob import TextBlob
from textblob import Word
import math

def doc_has_word(wrd, doc1):
    count=0
    if(doc1.words.count(wrd)>0):
        count+=1
    return count

s1=TextBlob("Hello there how are you Hello")
s2=TextBlob("Hi are you going to the fair? I have a feeling it will be great fair")

doclist=[s1,s2]
"""
for doc in doclist:

    wordlist=doc.words
    nowords=len(wordlist)
   
    for word in wordlist:
        termfrequency = doc.words.count(word)
        normtf=(float)(termfrequency)/(float)(nowords)
        print "The word: ", word,":   is repeated ",termfrequency, " times and the normalized TF is: ", normtf
    print"----------------------------------------------------"
"""

#testing IDF with a given word and set of docs in doclist
wordset=[]
for doc in doclist:
    wordset+=list(set(doc.words))

for word in wordset:
    docs_with_word=0
    for doc in doclist:
        docs_with_word+=doc_has_word(word,doc)

    idf = 1 + math.log((float)(len(doclist))/(float)(docs_with_word))
    print "Doclist: ",len(doclist),"   Docs containing word: ", word, "  ",docs_with_word, "   IDF: ", idf


