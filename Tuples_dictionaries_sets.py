Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4)
>>> b=('a','b','c','d')
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.append(c)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b.append(c)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.sort(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b.sort(a)
AttributeError: 'tuple' object has no attribute 'sort'
>>> a.pop(6)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.pop(6)
AttributeError: 'tuple' object has no attribute 'pop'
>>> b.remove('a')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b.remove('a')
AttributeError: 'tuple' object has no attribute 'remove'
>>> a.reverse(3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.reverse(3)
AttributeError: 'tuple' object has no attribute 'reverse'
>>> 
>>> for x in a:
	print(x)

	
1
2
3
4
>>> 
>>> c=list
>>> c=list(a)
>>> c
[1, 2, 3, 4]
>>> 
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> 
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> 'b' in b
True
>>> 'e' in b
False
>>> 1 in a
True
>>> 8 in a
False
>>> 
>>> x=[1,2,3,4]
>>> y=(x)
>>> y
[1, 2, 3, 4]
>>> x
[1, 2, 3, 4]
>>> y=(z for z in x)
>>> y
<generator object <genexpr> at 0x01F3D930>
>>> 
>>> a=[1,2,3,1,,4,2,5,3,7]
SyntaxError: invalid syntax
>>> a=[1,2,3,1,4,2,5,3,7]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c={'a','b','a','c','c'}
>>> c
{'b', 'a', 'c'}
>>> d=
SyntaxError: invalid syntax
>>> 
>>> d={'a','A','b','B'}
>>> D
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> d={'a','A','b','B'}
>>> d
{'B', 'b', 'A', 'a'}
>>> 
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.add(3)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s2.remove(7)
KeyError: 7
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.intersection(s2)
{3}
>>> s2.intersection(s1)
{3}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s2.add(3,5)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s2.add(3,5)
TypeError: add() takes exactly one argument (2 given)
>>> s1.extend(8,9,6)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s1.extend(8,9,6)
AttributeError: 'set' object has no attribute 'extend'
>>> s4=range(10,20)
>>> s3=
SyntaxError: invalid syntax
>>> s3={}
>>> s3={x for x in s4}
>>> s3
{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
>>> 
>>> s1.update({10,11,12})
>>> s1
{1, 2, 3, 10, 11, 12}
>>> s3={}
>>> s3
{}
>>> s4={}
>>> s4
{}
>>> codes={'Kenya':254, 'Uganda':256, 'Tanzania':255}
>>> codes['Kenya']
254
>>> codes['Uganda']
256
>>> codes['Tanzania']
255
>>> codes['Kenya']=250
>>> codes
{'Kenya': 250, 'Uganda': 256, 'Tanzania': 255}
>>> codes['Kenya']=254
>>> codes
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255}
>>> codes['Rwanda']=252
>>> codes
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255, 'Rwanda': 252}
>>> codes.pop('Rwanda')
252
>>> codes
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255}
>>> codes.keys()
dict_keys(['Kenya', 'Uganda', 'Tanzania'])
>>> codes.values()
dict_values([254, 256, 255])
>>> 
>>> for x in codes.keys()
SyntaxError: invalid syntax
>>> for key in codes.keys()
SyntaxError: invalid syntax
>>> codes.keys()
dict_keys(['Kenya', 'Uganda', 'Tanzania'])
>>> for key in codes.keys():
	print(key)

	
Kenya
Uganda
Tanzania
>>> 
>>> for x in codes.keys():
	print(x)

	
Kenya
Uganda
Tanzania
>>> 
>>> for v in codes.values():
	print(v)

	
254
256
255
>>> 
>>> m=dict()
>>> m['a']=10
>>> m['b']=20
>>> m
{'a': 10, 'b': 20}
>>> 
>>> g=range(0,10)
>>> g=dict()
>>> for x in g:
	h['x']=x*x
	print(x)

	
>>> g
{}
>>> g=dict(range(0,10))
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    g=dict(range(0,10))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> 
>>> g=range(0,10)
>>> g
range(0, 10)
>>> g=range(0,10)
>>> for x in g:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> g
range(0, 10)
>>> j=[x*x for x in g]
>>> j
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> k=dict()
>>> k['x' for x in g]=[x for x in j]
SyntaxError: invalid syntax
>>> k['g']=[x for x in j]
>>> k
{'g': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]}
>>> 
>>> g=range(0,10)
>>> j=[x*x for x in g]
>>> k={["y for y in g"]:[x*x for x in g]}
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    k={["y for y in g"]:[x*x for x in g]}
TypeError: unhashable type: 'list'
>>> k={[y for y in range(0,10)] : [x*x for x in g]}
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    k={[y for y in range(0,10)] : [x*x for x in g]}
TypeError: unhashable type: 'list'
>>> dict
<class 'dict'>
>>> k=dict()
>>> g=range(0,10)
>>> for x in g:
	print (x)

	
0
1
2
3
4
5
6
7
8
9
>>> j=[x*x for x in g]
>>> j
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> g=range(0,10)
>>> for y in g:
	print(y)

	
0
1
2
3
4
5
6
7
8
9
>>> for y,x in k.items():
	print(y,x)

	
>>> k
{}
>>> 
>>> g=range(0,10)
>>> j=[x*x for x in g]
>>> k=dict()
>>> k = {
	y for y in g: x*x for x in g
	
SyntaxError: invalid syntax
>>> k = {
	y for y in g: x*x for x in g}
	
SyntaxError: invalid syntax
>>> k.values=[y for y in g]
	
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    k.values=[y for y in g]
AttributeError: 'dict' object attribute 'values' is read-only
>>> k=dict()
	
>>> k=dict()
	
>>> k[x for x in g]=x*x
	
SyntaxError: invalid syntax
>>> 
	
>>> k[x for x in g] = [x*x for x in g]
	
SyntaxError: invalid syntax
>>> 
	
>>> k=dict()
	
>>> k[x for x in g] = j
	
SyntaxError: invalid syntax
>>> 
	
>>> k=dict()
	
>>> for x in g:
	k[x]=x*x
	print(k)

	
{0: 0}
{0: 0, 1: 1}
{0: 0, 1: 1, 2: 4}
{0: 0, 1: 1, 2: 4, 3: 9}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
	
>>> g=range(0,10)
	
>>> k=dict()
	
>>> for x in g:
	k[x]=x*x

	
>>> k
	
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
