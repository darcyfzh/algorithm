def romanToNum(str):
	sum = 0
	dic = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	for i in range(len(str) - 1):
		if str[i] < str[i + 1]:
			sum -= str[i]
		else:
			sum += str[i]
    sum += str[-1]
    return sum

