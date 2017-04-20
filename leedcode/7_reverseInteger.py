def reverseInt(x):
	if x == 0:
		return 0 
	rev = 0
	while(x != 0):
		rev = rev * 10 + x % 10
		x = x / 10
	return rev
