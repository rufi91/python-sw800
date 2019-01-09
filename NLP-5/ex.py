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



