"""
3. Using the following data, draw a bar chart to show monthwise High/Low temperature in Kerala state.
	Months should be in X axis. There should be two bars for each month, one for High and the other for Low. 

	Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec
High°C	32	32	33	33	32	30	30	30	30	30	31	31

Low°C	23	23	24	25	25	24	24	24	24	24	23	23

4. Draw a horizontal bar chart for the above problem.
"""
import matplotlib.pyplot as plt
import numpy as np


months=('Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec'.split())
months_l=np.arange(len(months))
high=[32,32,33,33,32,30,30,30,30,30,31,31]
low=[23,23,24,25,25,24,24,24,24,24,23,23]
bar_width=0.3

fig=plt.figure()
p1=fig.add_subplot(1,1,1)
"""
p1.bar(months_l, high, align='center', alpha =0.5, color='r',width=bar_width,label='high')
p1.bar(months_l+bar_width, low, align='center', alpha =0.5, color='c',width=bar_width,label='low')
p1.set_xticks(months_l)
p1.set_xticklabels(months)
p1.set_title("TEMPERATURE IN KERALA")
plt.show()
"""

p1.barh(months_l, high, align='center', alpha =0.5, color='r',height=0.3,label='high')
p1.barh(months_l+bar_width, low, align='center', alpha =0.5, height=bar_width,color='c',label='low')
p1.set_yticks(months_l)
p1.set_yticklabels(months)
p1.set_title("TEMPERATURE IN KERALA")
p1.set_xlabel("Deg C")
p1.set_ylabel("Months")
plt.show()
