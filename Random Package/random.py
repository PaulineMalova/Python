
def sumlist(n):
	d=[]
	for x in range(1,n):
		d.append(x)
		ans=sum(d)
	return (ans)




def divisibility(list,g,h):
	m=[]
	n=[]
	for x in list:
		if x%h==0 and x%g==0:
			m.append(x)
			n.append(x)	
		elif x%g==0:
			m.append(x)
		elif x%h==0:
			n.append(x)
		
	print (m)
	print (n)




def createdict(i):
	j=dict()
	for x in i:
		j[x]=x**3
	print (j)
		




