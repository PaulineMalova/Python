def List():
	x=[[1,2,4],[9,6,5],[8,3,7]]
	flat = []
	for y in x:
		for z in y:
			w = z
			flat.append(w)
			flat.sort()
	return (flat)	




def fruit_dict():
	fruits_list = ["mangoes","apples","oranges","bananas","pawpaws","melons"]
	g = dict()
	for fruit in fruits_list:
		g[fruit] = len(fruit)
	return g
	

def interest_calc(rate,time):
	loans = {"Irene":50000,"Joy":80000,"Beatrice":70000,"Shee":40000,"Cate":60000}
	for x in loans:
		interest = loans[x]*(rate/100)*time
		print("Dear {}, your loan has accumulated Ksh{} interest over the past {} years.".format(x,interest,time))
				