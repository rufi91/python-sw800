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

#plot"""
