"""
Create a module that contains functions for performing the following(use re).
 (Slno 1 to 6 should return boolean )
 1.IsInteger-Should take one parameter as string and should contain integer for True else False. 
 2.IsFloat-Should take one parameter as string and if it contains a float return True else False.
 3.HasVowel-supplied string should contain at least one vowel char for True else False.
 4.IsHex - supplied string should contain only hex digits,if so True else False.
 5.IsDate - True if given a date in DD-MM-YYYY format.
 6.IsValidPassword - True is the given string containas - 8 to 16 alphanumerics,at least 2 digits,at least 2 lowercase letters
			and atleast two uppercase letters  
 7.IsValidEmail-True if the given string is valid email id.
		
		
 8.Normalise -  to replace all instances of one or more whitespace characters with a single space.
 9.Normalisen-  to replace all instances of one or more whitespace characters with  n spaces.
		this function should take two parameters- string and n, make n def parameter with value 1.
 
 10.Test the module. """

import re

#1
def IsInteger(str1):
        if (re.match('.*\d.*',str1)):
            return 'True'
        else:
            return 'False'
  

#print IsInteger('abacabac')

#2
def IsFloat(str1):
    try:
        if (re.match(r'.*\d+\.\d+.*',str1).group() ):
            return 'True'
        else:
            return 'False'
    except:
        return 'False'

#print IsFloat('2.2')

#3
def HasVowel(str1):
           if (re.search('[aeiou]',str1, re.I)):
            return 'True'
           else:
            return 'False'

print HasVowel('223423I2342')


#4 Matches expression starting with a 0, following by either a lower or uppercase x, followed by one or more characters in the ranges 0-9, or a-f, or A-F
def IsHex(str1):
           if (re.search('\x\d\d',str1)):
            return 'True'
           else:
            return 'False'

print IsHex('223423i2342')

