
import xml.dom.minidom as dm

content = ""
dtree = dm.parse('book.xml')

books = dtree.getElementsByTagName("book")
i=1
for book in books:
    cat = book.getAttribute("category")
    title = book.getElementsByTagName("title")[0].firstChild.data
    author = book.getElementsByTagName("author")[0].firstChild.data
    year = book.getElementsByTagName("year")[0].firstChild.data
    price = book.getElementsByTagName("price")[0].firstChild.data
    para = "%d.The book %s belongs to %s category and is written by %s.\n    The book is published in the year %s with a price of %s.\n"%(i,title,cat,cat,year,price)
    content += para
    i += 1

print content 
    
f=open('book1.txt','w')
f.write(content)
f.close()
