Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="Posh"
>>> a[0]
'P'
>>> 
>>> def initials(first,last):
	f=first[0]
	j=last[0]
	init=f+j
	return init

>>> initials("Posh","Addah")
'PA'
>>> initials("Job","Brown")
'JB'
>>> 
>>> 
>>> initials("2010","4075")
'24'
>>> def initials(first,last):
	f=first[-1]
	j=last[-1]
	init=f+j
	return init

>>> initials("Posh","Addah")
'hh'
>>> 
