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
