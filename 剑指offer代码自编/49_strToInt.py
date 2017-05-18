def strToInt(a):
	if len(a) == 0 or a == None:
		return 
	num = 0
	if a[0] == '+'：
		positive = True
	if a[0] == '-':
		positive = False
	if a[1]:
		num = strToIntCore(a[1:], positive)
	return num	

def strToIntCore(a, positive):
	sum = 0
	i = 0
	while(a[i]):
		if '0'<= a[i] <= '9':
			if positive:
				flag = 1
			else:
				flag = -1
			sum = sum * 10 + flag * (a[i] - '0')
			i += 1
		else:
			sum = 0
			break
	return sum;

