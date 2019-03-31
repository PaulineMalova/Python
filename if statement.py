Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1={'name':'Pauline','balance':70000}
>>> customer2={'name':'Paul','balance':65000}
>>> customer3={'name':'Perlee','balance':60000}
>>> customer4={'name':'Peter','balance':55000}
>>> customer5={'name':'Patience','balance':50000}
>>> 
>>> customers=[customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'Pauline', 'balance': 70000}, {'name': 'Paul', 'balance': 65000}, {'name': 'Perlee', 'balance': 60000}, {'name': 'Peter', 'balance': 55000}, {'name': 'Patience', 'balance': 50000}]
>>> 
>>> for customer in customers:
	sms="Hi {}, your balance is {}.".format(customer['name'],customer['balance'])
	print(sms)

	
Hi Pauline, your balance is 70000.
Hi Paul, your balance is 65000.
Hi Perlee, your balance is 60000.
Hi Peter, your balance is 55000.
Hi Patience, your balance is 50000.
>>> 
>>> 
>>> for customer in customers:
	loanlimit=customer['balance']//2.9
	sms="Hi {}, your balance is {}. You have qualified to borrow {}. Thank you.".format(customer['name'],customer['balance'],loanlimit)
	print(sms)

	
Hi Pauline, your balance is 70000. You have qualified to borrow 24137.0. Thank you.
Hi Paul, your balance is 65000. You have qualified to borrow 22413.0. Thank you.
Hi Perlee, your balance is 60000. You have qualified to borrow 20689.0. Thank you.
Hi Peter, your balance is 55000. You have qualified to borrow 18965.0. Thank you.
Hi Patience, your balance is 50000. You have qualified to borrow 17241.0. Thank you.
>>> 
>>> 
>>> for x in range(0,10):
	if x%3 ==0:
		print(x)

		
0
3
6
9
>>> 
>>> for x in range(0,10:)
SyntaxError: invalid syntax
>>> 
>>> for x in range(0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> 
>>> for x in range(0,10):
	if x%3 == 0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> 
>>> for x in range(0,20):
	if x%3 == 0:
		print("{} is divisible by 3".format(x))
	elif x%5 == 0:
		print("{} is divisible by 5".format(x))
	else:
		print("{} is neither divisible by 3 nor 5".format(x))

		
0 is divisible by 3
1 is neither divisible by 3 nor 5
2 is neither divisible by 3 nor 5
3 is divisible by 3
4 is neither divisible by 3 nor 5
5 is divisible by 5
6 is divisible by 3
7 is neither divisible by 3 nor 5
8 is neither divisible by 3 nor 5
9 is divisible by 3
10 is divisible by 5
11 is neither divisible by 3 nor 5
12 is divisible by 3
13 is neither divisible by 3 nor 5
14 is neither divisible by 3 nor 5
15 is divisible by 3
16 is neither divisible by 3 nor 5
17 is neither divisible by 3 nor 5
18 is divisible by 3
19 is neither divisible by 3 nor 5
>>> 
>>> 
>>> for x in range(0,100):
	if x%7 == 0:
		print("{} is divisible by 7".format(x))

		
0 is divisible by 7
7 is divisible by 7
14 is divisible by 7
21 is divisible by 7
28 is divisible by 7
35 is divisible by 7
42 is divisible by 7
49 is divisible by 7
56 is divisible by 7
63 is divisible by 7
70 is divisible by 7
77 is divisible by 7
84 is divisible by 7
91 is divisible by 7
98 is divisible by 7
>>> 
>>> for x in range(0,20):
	if x%3 == 0 and x%5 == 0:
		print(x)

		
0
15
>>> 
>>> for x in range(0,20):
	if x%3 == 0 or x%5 == 0:
		print(x)

		
0
3
5
6
9
10
12
15
18
>>> 
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> 
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> 
>>> for x in range(900,950):
	if x%3 == 0 and x%5 == 0:
		print("Fizzbuzz")
	elif x%5 == 0:
		print("Fizz")
	elif x%3 == 0:
		print("buzz")
	else:
		print(x)

		
Fizzbuzz
901
902
buzz
904
Fizz
buzz
907
908
buzz
Fizz
911
buzz
913
914
Fizzbuzz
916
917
buzz
919
Fizz
buzz
922
923
buzz
Fizz
926
buzz
928
929
Fizzbuzz
931
932
buzz
934
Fizz
buzz
937
938
buzz
Fizz
941
buzz
943
944
Fizzbuzz
946
947
buzz
949
>>> 
