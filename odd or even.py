def odd_or_even(arr):
	x = sum(i for i in arr)
	print(x)
	if x % 2 > 1:
		return 'odd'
	else: 
		' even'

odd_or_even()