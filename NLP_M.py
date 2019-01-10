############################################## TFIDF DAY5 ####################################
"""
1.  Have a list of minimum 5 sentences. Find how close they are to a query string using tfidfVectorizer and cosine_similarity.
2. Modify the program to read strings from files.
"""
def locateLargest(matrix):
    largest_num = None 
    row = None
    col = None

    for row_idx, row in enumerate(matrix):
        for col_idx, num in enumerate(row):
            if num==1:
                num=-100
            elif num > largest_num or largest_num is None:

                largest_num = num
                row = row_idx
                col = col_idx

    return (largest_num, row, col)

#1

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
"""
s1="Word embeddings allow us to easily compute the semantic similarity between two words, or to find the words most similar to a target word. Here we’ll compare the most popular ways of computing sentence similarity and investigate how they perform."
s2="Mangoes are juicy stone fruit (drupe) from numerous species of tropical trees belonging to the flowering plant genus Mangifera, cultivated mostly for their edible fruit"
s3="Mango trees grow to 35–40 m (115–131 ft) tall, with a crown radius of 10 m (33 ft). The trees are long-lived, as some specimens still fruit after 300 years"
s4= "Ripe intact mangoes give off a distinctive resinous, sweet smell"
s5= "Mangoes have been cultivated in South Asia for thousands of years and reached Southeast Asia between the fifth and fourth centuries BCE. By the 10th century CE"
"""
#2
f=open('d1.txt','r')
s1=str(f.readlines())
f=open('d2.txt','r')
s2=str(f.readlines())
f=open('d3.txt','r')
s3=str(f.readlines())
print s1,s2,s3

query="Mangoes tropical fruit cultivated century"
#query="Word embeddings allow us to easily compute the semantic similarity between two words"

#sentences=[s2,s1,s3,s4,s5, query]
sentences=[s1,s2,s3,query]

tfidVec=TfidfVectorizer()
matrix=tfidVec.fit_transform(sentences)
dict_sent=tfidVec.vocabulary_
print "\nTotal number of unique words: ", len(dict_sent)

for key in dict_sent.keys():
    print key, " :", dict_sent[key]

print "\nMatrix after fit_transform: \n", matrix

kmatrix=cosine_similarity(matrix[-1],matrix)
print "\nMatrix after cosine_similarity: \n", kmatrix

value, row, col= locateLargest(kmatrix)
print "\ndoc # %d has most similartiy of %f"%(col+1,value)

################################################### DAY 6 SUBJECTIVITY POLARITY ##################################################################
"""
1. Take a sentence as input. Display  the Subjectivity and the Polarity of the statement.
2. If the subjectivity is 0.0 display "It is a Fact"
    If the subjectivity is not 0 , if the polarity lies between 0 and 1 display "Positive", if the polarity lies between -1 and 0 display "Negative", if the polarity is equal to 0 display "Neutral".
"""
from textblob import TextBlob

s1="Lucy is a good girl"
s2="The world is flat"
s3="The world is a good place"
s4="The actors are briliant and the storyline is engrossing. Yet the movie fails to be a masterpeice "
s5="The sky is blue"
sentenceList=[s1,s2,s3,s4,s5]
for s in sentenceList:
	s=TextBlob(s)
	print s, ": "
	if s.sentiment.subjectivity==0:
                print "Subjectivity: This is a fact\n"
        elif s.sentiment.polarity<0:
                print "Polarity: Negative \n"
        elif s.sentiment.polarity>0:
                print "Polarity: Positivie \n"
        else:
                print "Polarity: Neutral"

###############################################DAY7 CLUSTERING COSINE SIMILARITY ########################################################
"""
1. Create a few sentences . Find the frequency count of the words in the vocabulary.
4. Visualise the results.
"""
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

#create data
s1="Word embeddings allow us to easily compute the semantic similarity between two words, or to find the words most similar to a target word. Here we’ll compare the most popular ways of computing sentence similarity and investigate how they perform."
s2="Mangoes are juicy stone fruit (drupe) from numerous species of tropical trees belonging to the flowering plant genus Mangifera, cultivated mostly for their edible fruit"
#s3="Mango trees grow to 35–40 m (115–131 ft) tall, with a crown radius of 10 m (33 ft). The trees are long-lived, as some specimens still fruit after 300 years"
#s4= "Ripe intact mangoes give off a distinctive resinous, sweet smell"
s5= "Mangoes have been cultivated in South Asia for thousands of years and reached Southeast Asia between the fifth and fourth centuries BCE. By the 10th century CE"

doc_list= [s5,s1,s2]
print doc_list
#find frequency count
cVec=CountVectorizer(stop_words='english')
count_matrix= cVec.fit_transform(doc_list)


#print word count frequency
count_matrix=count_matrix.toarray()
count=([sum(count_matrix) for count_matrix in zip(*count_matrix)])
l1=list(zip(count, cVec.get_feature_names()))
for x,y in l1:
    print x,": ",y


#2. Cluster the words in the sentences  based on the count.
dict_words=cVec.vocabulary_
#dict_words.keys(),count
X=list(zip(count,dict_words.values()))

model=KMeans(n_clusters=2)
model.fit(X)

#plt.scatter(count,dict_words.values(),  s=50, c=model.labels_)
#plt.show()

#3. Modify the program to cluster sentences based on cosine similarity.

tfidVec=TfidfVectorizer()
matrix=tfidVec.fit_transform(doc_list)
cos_matrix=cosine_similarity(matrix[-1],matrix)
label=np.arange(len(doc_list))
print label, cos_matrix.flatten()
X1=list(zip(label,cos_matrix.flatten()))
print X1

model1=KMeans(n_clusters=2)
model1.fit(X1)

plt.scatter(label,cos_matrix, c=model1.labels_)
plt.show()



"""
for j in range(count_matrix.shape[1]):
    for i in range(count_matrix.shape[0]):
        print count_m_names[j], ": ", count_matrix[i][j]
         
         
#for key in count_matrix.keys():
 #   print key, " :", count_matrix[key]
#tfid
tfidVec=TfidfVectorizer()
matrix=tfidVec.fit_transform(doc_list)
dict_sent=tfidVec.vocabulary_
#print "\nTotal number of unique words: ", len(dict_sent)
#for key in dict_sent.keys():
 #   print key, " :", dict_sent[key]
#create train model
#cosinse similarity
"""

#################################################DAY 4 TF IDF###########################################
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

##################################DAY 3 NBCLASSIFIER TEXT CLASSIFICATION###############################
from textblob.classifiers import NaiveBayesClassifier

trainData=[]
f=open('medidata.txt','r')
data= f.readline().strip()
while data:
    splitdata=data.split(',')
    category = splitdata[0]
    desc=splitdata[1]
    tuple1= desc,category
    trainData.append(tuple1)
    data=f.readline().strip()

nbclass = NaiveBayesClassifier(trainData)
print trainData
txt=""" Measles antibody: reevaluation of protective titers.
 A school blood drive before a measles outbreak permitted correlation of preexposure measles antibody titers with clinical protection using the plaque reduction neutralization (PRN) test and an EIA.
 Of 9 donors with detectable preexposure PRN titer less than or equal to 120, 8 met the clinical criteria for measles (7 seroconfirmed) compared with none of 71 with preexposure PRN titers greater than 120 (P less than .0001).
 Seven of 11 donors with preexposure PRN titers of 216-874 had a greater than or equal to 4-fold rise in antibody titer (mean, 43-fold) compared with none of 7 with a preexposure PRN titer greater than or equal to 1052 (P less than .02).
 Of 37 noncases with preexposure PRN titer less than 1052, 26 (70%) reported one or more symptoms compared with 11 (31%) of 35 donors with preexposure PRN titers greater than or equal to 1052 (P less than .002).
 By EIA, no case had detectable preexposure antibody; the preexposure geometric mean titer of asymptomatic donors (220) was not significantly higher than that of symptomatic donors who did not meet the clinical criteria for measles (153) (P = .10).
 The study suggests that PRN titers less than or equal to 120 were not protective against measles disease and illness without rash due to measles may occur in persons with PRN titers above this level."""


testclass=nbclass.classify(txt)
if testclass == 'C01':
    print("\n Text belongs to category BACTERIAL INFECTIONS AND MYCOSES", nbclass.classify(txt), "")
if testclass == 'C02':


############################################### TEXT SUMMARY ABSTRACT #####################################

#4
from textblob import TextBlob;
f=open("sample.txt","r");
thePara = f.read();
theText = TextBlob(thePara);
print("# of sentences: " + str(len(theText.sentences)));
print("# of words: " + str(len(theText.words)));

nounList = set();
for word, tag  in theText.tags:
	if (tag == "NN" or tag == "NNS"):
		nounList.add(word);

aString = "";
for noun in nounList:
	aString = noun +" ," +  aString
aString = "The text is about: " + aString;
print(aString);

#Summary of important sentences
len = len(theText.sentences);
theSentence = theText.sentences;
print("_________Abstract____________");
summary =theSentence[0] +" " + theSentence[len-1];
print(summary);
