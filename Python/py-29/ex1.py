"""
2. Show partywise seat share for following results of the Assembly Elections 2018
in a piechart.Party with highest percentage should be shown as detached (slightly). 

Madhya Pradesh	
	INC - Win (114)
        BJP - Win (15)
        Independent - Win (4)
        Others - Win (3)	
Rajasthan	
	INC - Win (99)
	BJP- Win (73)
	Independent- Win (3)
	Others- Win (14)
Chhattisgarh	
	INC- Win (68)
	BJP- Win (15)
	BSP+- Win (9)
	Others- Win (7)	
Telangana	
	TRS- Win (88)
	INC- Win (19)
	BJP- Win (1)
	Others- Win (11)	
Mizoram	
	MNF- Win (26)
	INC- Win (5)
	BJP- Win (1)
	Others- Win (8)	
"""

import matplotlib.pyplot as plt

expl=[0.1,0,0,0]
fo=plt.figure(figsize=(8,8))

mp_party=('INC BJP INDEPENDANT OTHERS'.split())
mp_seat=[114,15,4,3]
sp1= fo.add_subplot(2,2,1)
sp1.set_title("MADHYA PRADESH")
sp1.pie(mp_seat, autopct='%1.1f%%', labels=mp_party, explode=expl)

raj_party=('INC BJP INDEPENDANT OTHERS'.split())
raj_seat=[99,73,3,14]
sp2= fo.add_subplot(2,2,2)
sp2.set_title("RAJASTHAN")
sp2.pie(raj_seat, autopct='%1.1f%%', labels=raj_party, explode=expl)

ch_party=('INC BJP BSP+ OTHERS'.split())
ch_seat=[68,15,9,7]
sp3= fo.add_subplot(2,2,3)
sp3.set_title("CHHATTISGARH")
sp3.pie(ch_seat, autopct='%1.1f%%', labels=ch_party, explode=expl)

t_party=('TRS INC BJP OTHERS'.split())
t_seat=[88,19,1,11]
sp3= fo.add_subplot(2,2,4)
sp3.set_title("TELENGANA")
sp3.pie(t_seat, autopct='%1.1f%%', labels=t_party, explode=expl)

plt.show()




