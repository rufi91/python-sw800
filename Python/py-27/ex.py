"""
1. Import the necessary libraries

2. Import the dataset(drinks.csv) from common/Python_Exercise folder.

3. Assign it to a variable called drinks.

4. Print the continent that drinks more beer on average?

5. For each continent print the statistics(count,mean,std etc.) for wine consumption.

6. Print the mean alcoohol consumption per continent for every column

7. Print the median alcoohol consumption per continent for every column

8. Print the mean, min and max values for spirit consumption.
"""
import pandas as pd

drinks=pd.read_csv('/home/ai21/Desktop/common/Python_Exercises/drinks.csv')
drinkobj=drinks.groupby('continent')


print "\nPrint the continent that drinks more beer on average: ", drinkobj.sum()['beer_servings'].max()
print drinkobj.sum()['beer_servings'].nlargest(1)
print drinkobj.sum()['beer_servings'].idxmax()

print "\n\nFor each continent print the statistics(count,mean,std etc.) for wine consumption.:\n",drinkobj.describe()['wine_servings']

print "\n\nPrint the mean alcoohol consumption per continent for every column:\n",drinkobj.mean()

print "\nmedian alcoohol consumption per continent for every column\n", drinkobj.agg('median')

print "\n\n Print the mean, min and max values for spirit consumption.: \n", drinkobj.agg(['mean','min','max'])['spirit_servings']

print "\n\n"


