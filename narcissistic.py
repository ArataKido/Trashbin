
def narcissistic( value ):
	n = [int(i) for i in str(value)]
	
	x = [n[i]**len(n) for i in range(0, len(n))]
	output = 0
	for i in range(len(x)):
		output += x[i]
	if output==value:
		return True 
	else: 
		return False 

narcissistic(153)