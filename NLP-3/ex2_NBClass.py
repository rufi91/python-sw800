from textblob.classifiers import NaiveBayesClassifier
import os
trainData=[]
count=0

for i in range(1,10):
    folderpath='/home/ai21/Desktop/common/NLP/NLP3/Assignment 3/C0%d'% i
    
    for file in os.listdir(folderpath):
        count+=1
        filepath = os.path.join(folderpath, file)
        f=open(filepath,'r')
        data= f.readlines()
        category = 'C0%d'% i
        tuple1= data,category
        trainData.append(tuple1)
        if (count==2):
            break;

print len(trainData)
    
nbclass = NaiveBayesClassifier(trainData)

txt="""
External fixation for type III open tibial fractures.
 An analysis of 51 type III open tibial fractures treated by external skeletal fixation is presented.
 The fractures are subdivided according to the classification of Gustilo, Mendoza and Williams (1984) into types IIIa, IIIb and IIIc.
 The different prognoses of these fracture subtypes is examined.
 The use of the Hoffmann and Hughes external fixators in the management of type III open tibial fractures is presented and it is suggested that the prognosis is independent of the type of fixator used.
 """
testclass=nbclass.classify(txt)
print testclass
"""
if testclass == 'C01':
    print("\n Text belongs to category BACTERIAL INFECTIONS AND MYCOSES", nbclass.classify(txt), "")
if testclass == 'C02':
    print("\n Text belongs to category VIRUS DISEASES", nbclass.classify(txt), "")
"""
