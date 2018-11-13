import xml.sax

f= open("parsebook.txt","w+")
class ourhandler(xml.sax.ContentHandler):
 
 def __init__(self):
    self.title=''
    self.category=''
    self.author=''
    self.year=''
    self.price=''
    self.currtag=''
    self.count=0
    
 def startElement (self, tagname, attrs):
    self.currtag=tagname
    if tagname == 'book':
     self.category= attrs['category']
     self.count+=1

 def characters(self, content):
    if self.currtag == 'title':
     self.title=content   
    if self.currtag == 'author':
     self.author=content
    if self.currtag == 'year':
     self.year=content
    if self.currtag == 'price':
     self.price=content

 def endElement(self, tag): 
    if tag == 'title':
     var=str(self.count), ". The book ",self.title, " belongs to the ", self.category," category "
     f.writelines(var)
    if tag == 'author':
     var= " and is written by ", self.author
     f.writelines(var)
    if tag == 'year':
     var= ". This book is published in the year ", self.year
     f.writelines(var)
    if tag == 'price':
     var= " with a price of ", self.price, ".\n"
     f.writelines(var)

#f= open("newbook.txt","w+")
parobj= xml.sax.make_parser()
ourhandlerobj=ourhandler()
parobj.setContentHandler(ourhandlerobj)
parobj.parse("/home/ai21/Desktop/common/Python_Exercises/book.xml")


