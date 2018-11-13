
import xml.dom.minidom as dm

dtree = dm.parse('note.xml')

root_n = dtree.documentElement

def parse(node):
    if node.nodeType == 3:
        print node.parentNode.nodeName," : ",node.nodeValue
    else:
        for ch in node.childNodes:
            parse(ch)


parse(root_n)
