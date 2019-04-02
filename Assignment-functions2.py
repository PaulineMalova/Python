Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sumlist(n):
	f=[]
	for x in range(1,n+1):
		f.append(x)
		a=sum(f)
	return a

>>> sumlist(100)
5050
>>> sumlist(20)
210
>>> 
>>> 
>>> def functionName(lists,i):
	d=[]
	e=[]
	for x in lists:
		if x%i==0:
			d.append(x)
		else:
			e.append(x)
	print("The list of numbers divisible by the integer: {}".format(d))
	print("The list of numbers not divisible by the integer: {}".format(e))

	
>>> a=[1,2,3,4,5]
>>> functionName(a,2)
The list of numbers divisible by the integer: [2, 4]
The list of numbers not divisible by the integer: [1, 3, 5]
>>> 
>>> b=range(0,20)
>>> for x in b:
	functionName(b,2)

	
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> for x in b:
	k=[]
	c=functionName(b,2)
	k.append(c)

	
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
The list of numbers divisible by the integer: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list of numbers not divisible by the integer: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
