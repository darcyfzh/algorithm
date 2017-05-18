def find(a, number):
	found = True
	if a == None or a == [[]] or a = []:
		return False
	rows = len(a)
	cols = len(a[0])
	row = 0
	col = cols - 1
	while(row < rows and col >= 0):
		if a[row][col] == number:
			return found
			break
		elif a[row][col] < number:
			row += 1
		else:
			col -= 1
	return found
