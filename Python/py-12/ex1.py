"""
The book Think Python belongs to python category and is written by AB downy.
      This book is published in the year 2015 with a price of 300.
      """

import xml.dom.minidom as dm

f= open("dombook.txt","w+")
dtree=dm.parse('/home/ai21/Desktop/common/Python_Exercises/book.xml')
root= dtree.documentElement

booknodes=root.getElementsByTagName('book')
for bn in booknodes:
    titlenodes = bn.getElementsByTagName('title')
    for tn in titlenodes:
        authornodes = bn.getElementsByTagName('author')
    for an in authornodes:
        yearnodes = bn.getElementsByTagName('year')
    for yn in yearnodes:
        pricenodes = bn.getElementsByTagName('price')
    for pn in pricenodes:
        var= "\n",tn.childNodes[0].nodeValue, an.childNodes[0].nodeValue,yn.childNodes[0].nodeValue,pn.childNodes[0].nodeValue,
        f.writelines(var)

"""
for i in range (0,len(category)):
      var= "The book ",str(titles[i]), " belongs to ", str(category[i])," category and is written by ", str(author[i]),". This book is published in the year ", str(pubyear[i]), " with a price of ", str(price[i]),"."
      print str(var)
      f.writelines(str(var))
"""

