

#1
#from textblob import Word;
#var= Word(raw_input("Enter a singular noun: "));
#print(var.pluralize());

#2
#var1= Word(raw_input("Enter a plural noun: "));
#print(var1.singularize());

""" #3
from textblob import TextBlob;
sampleSent =  TextBlob(raw_input("Enter a sentence: "));
for word, tag in sampleSent.tags :
	print("Word: "+ word + " POS: " + tag); """

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

