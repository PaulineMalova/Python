Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits=['orange','mango','pawpaw','melon','strawberry','avocado','pears','banana','pineapple','guavas']
>>> len(x for x in fruits)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len(x for x in fruits)
TypeError: object of type 'generator' has no len()
>>> len('orange')
6
>>> len(['x' for 'x' in fruits])
SyntaxError: can't assign to literal
>>> 
>>> g=dict()
>>> for x in fruits:
	g[x]=len(x)

	
>>> g
{'orange': 6, 'mango': 5, 'pawpaw': 6, 'melon': 5, 'strawberry': 10, 'avocado': 7, 'pears': 5, 'banana': 6, 'pineapple': 9, 'guavas': 6}
>>> 
