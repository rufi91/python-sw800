"""
3.Write a python script(using numpy) to solve the following.

		A group of people took a trip on a bus at Rs.3.00 per child and Rs.3.20 per adult for 
 		a total of Rs.118.40
 		They took the train back at Rs.3.50 per child and Rs.3.60 per adult for 
		a total of Rs.135.20
		Print the number of children and adults.
		(hint : matrix multiplication and inverse to get the effect of division)

"""

import numpy as np

prices=np.array([[3,3.5],[3.2,3.6]])
total=np.array([118.4,135.2])
people= total.dot(np.linalg.inv(prices))

print people
