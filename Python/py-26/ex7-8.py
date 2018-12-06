"""
7.From the given csv files(items.csv and sales.csv in common/Python_Exercises folder) create two dataframe objects- idf1 and sdf1

8.Using idf1 and sdf1 print item name, region and sales quantity and store the same in a new dataframe.

9.Create two dataframes by applying pivot on the above dataframe with region/item name as index/column.
"""
import pandas as pd

idf1=pd.read_csv('/home/ai21/Desktop/common/Python_Exercises/items.csv')
sdf1=pd.read_csv('/home/ai21/Desktop/common/Python_Exercises/sales.csv')

print idf1.columns, sdf1.columns

mdf1=idf1.merge(sdf1, left_on='id', right_on='tid')[['name','region','sale_qty']]
print mdf1

df1=mdf1.pivot(index='region',columns='name')
print df1

df2=mdf1.pivot(columns='region',index='name')
print "\n\n",df2
