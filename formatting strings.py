Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "AKIRACHIX"
>>> a
'AKIRACHIX'
>>> b = "akirachix"
>>> b
'akirachix'
>>> a.isupper()
True
>>> b.isupper()
False
>>> a.islower()
False
>>> b.islower()
True
>>> first = "Pauline"
>>> last = "Brown"
>>> school = "AkiraChix"
>>> print("Hello {}{} Welcome to {}".format(first, last, school))
Hello PaulineBrown Welcome to AkiraChix
>>> print("Hello {} {}! Welcome to {}.".format(first,last,school))
Hello Pauline Brown! Welcome to AkiraChix.
>>> year = 1995
>>> current = 2019
>>> age = "current-year"
>>> age
'current-year'
>>> age = "current - year"
>>> age
'current - year'
>>> age = current-year
>>> age
24
>>> print("Hello {} you are {} years old.".format(first,age))
Hello Pauline you are 24 years old.
>>> 
>>> 
>>> 
>>> c1="kenya"
>>> c2="Uganda"
>>> c3="Tanzania"
>>> ke_code = "254"
>>> tz_code = "255"
>>> ug_code = "256"
>>> c1
'kenya'
>>> ke_code
'254'
>>> 
>>> print("{}'s code is {}".format(c1,ke_code))
kenya's code is 254
>>> 
>>> print("{}'s code is {}.".format(c3,tz_code))
Tanzania's code is 255.
>>> 
>>> print("{}'s code is {}.".format(c2,ug_code))
Uganda's code is 256.
>>> 
>>> print("{}'s code is
	  
SyntaxError: EOL while scanning string literal
>>> print("{}'s code is {}".format(c1,ke_code))
	  
kenya's code is 254
>>> print("{}'s code is {}".format(c2,ug_code))
	  
Uganda's code is 256
>>> 
	  
>>> print("{}'s code is {}.".format(c1,ke_code)) \n ("{}'s code is {}.".format(c3,tz_code))
	  
SyntaxError: unexpected character after line continuation character
>>> print("{}'s code is {}.".format(c1,ke_code)) "\n" ("{}'s code is {}.".format(c3,tz_code))
	  
SyntaxError: invalid syntax
>>> 
	  
>>> print("{}'s code is {}." \n "{}'s code is {}." \n "{}'s code is {}.".format(c1,ke_code,c2,ug_code,c3_tz_code))
	  
SyntaxError: unexpected character after line continuation character
>>> 
	  
>>> print("{}'s code is {}. \n {}'s code is {}. \n {}'s code is {}.".format(c1,ke_code,c2,ug_code,c3_tz_code))
	  
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print("{}'s code is {}. \n {}'s code is {}. \n {}'s code is {}.".format(c1,ke_code,c2,ug_code,c3_tz_code))
NameError: name 'c3_tz_code' is not defined
>>> 
	  
>>> print("{}'s code is {} \n {}'s code is {} \n {}'s code is {}".format(c1,ke_code,c2,ug_code,c3_tz_code))
	  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print("{}'s code is {} \n {}'s code is {} \n {}'s code is {}".format(c1,ke_code,c2,ug_code,c3_tz_code))
NameError: name 'c3_tz_code' is not defined
>>> 
	  
>>> print("()'s code is () \n ()'s code is () \n ()'s code is ()".format(c1,ke_code,c2,ug_code,c3_tz_code))
	  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print("()'s code is () \n ()'s code is () \n ()'s code is ()".format(c1,ke_code,c2,ug_code,c3_tz_code))
NameError: name 'c3_tz_code' is not defined
>>> print("{} code is {} \n {} code is {} \n {} code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
kenya code is 254 
 Uganda code is 256 
 Tanzania code is 255
>>> 
	  
>>> print("{}'s code is {} \n {}'s code is {} \n {}'s code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
kenya's code is 254 
 Uganda's code is 256 
 Tanzania's code is 255
>>> 
