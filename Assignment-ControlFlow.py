Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> for x in range(0,100):
	if x%9 == 0:
		a.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> 
>>> b=[]
>>> for x in range(0,100):
	if x%11 == 0:
		b.append(x)

		
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c.sort()
>>> c
[0, 0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99, 99]
>>> 
>>> 
>>> 
>>> d=[]
>>> for x in range(2019,2019):
	if x%4 == 0:
		d.append(x)

		
>>> d
[]
>>> for x in range(2019,2119):
	if x%4 == 0:
		d.append(x)

		
>>> d
[2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2100, 2104, 2108, 2112, 2116]
>>> 
>>> 
>>> 
>>> student1={'name':'Pauline','Y.O.B':1998}
>>> student2={'name':'Addah','Y.O.B':1996}
>>> student3={'name':'Sheldon','Y.O.B':1995}
>>> student4={'name':'Purity','Y.O.B':1994}
>>> student5={'name':'Philice','Y.O.B':1999}
>>> 
>>> students=[student1,student2,student3,student4,student5]
>>> students
[{'name': 'Pauline', 'Y.O.B': 1998}, {'name': 'Addah', 'Y.O.B': 1996}, {'name': 'Sheldon', 'Y.O.B': 1995}, {'name': 'Purity', 'Y.O.B': 1994}, {'name': 'Philice', 'Y.O.B': 1999}]
>>> 
>>> 
>>> age=2019-['Y.O.B']

>>> for student in students:
	ageindays = (2019-student['Y.O.B'])*365
	print("Hi {}, You were born in {} thus you have lived for {} days.".format('name','Y.O.B',ageindays))

	
Hi name, You were born in Y.O.B thus you have lived for 7665 days.
Hi name, You were born in Y.O.B thus you have lived for 8395 days.
Hi name, You were born in Y.O.B thus you have lived for 8760 days.
Hi name, You were born in Y.O.B thus you have lived for 9125 days.
Hi name, You were born in Y.O.B thus you have lived for 7300 days.
>>> for student in students:
	ageindays = (2019-student['Y.O.B'])*365
	print("Hi {}, You were born in {} thus you have lived for {} days.".format([student'name','Y.O.B'],ageindays))
	
SyntaxError: invalid syntax
>>> for student in students:
	ageindays = (2019-student['Y.O.B'])*365
	print("Hi {}, You were born in {} thus you have lived for {} days.".format(student['name','Y.O.B'],ageindays))

	
Traceback (most recent call last):
  File "<pyshell#53>", line 3, in <module>
    print("Hi {}, You were born in {} thus you have lived for {} days.".format(student['name','Y.O.B'],ageindays))
KeyError: ('name', 'Y.O.B')
>>> for student in students:
	ageindays = (2019-student['Y.O.B'])*365
	print("Hi {}, You were born in {} thus you have lived for {} days.".format(student['name'],student['Y.O.B'],ageindays))

	
Hi Pauline, You were born in 1998 thus you have lived for 7665 days.
Hi Addah, You were born in 1996 thus you have lived for 8395 days.
Hi Sheldon, You were born in 1995 thus you have lived for 8760 days.
Hi Purity, You were born in 1994 thus you have lived for 9125 days.
Hi Philice, You were born in 1999 thus you have lived for 7300 days.
>>> 
