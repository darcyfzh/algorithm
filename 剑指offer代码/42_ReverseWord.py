'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: Reverse word sentence
'''
def reverseSentence(a):
	a.reverse()
	str = ''
	for i in range(len(a)):
		str += a[i]
		str += ' '
	return str

def leftRotating(a, k):
	temp1 = a[:k]
	temp1 = temp1[::-1]
	temp2 = a[k:]
	temp2 = temp2[::-1]
	new = temp1 + temp2
	new = new[::-1]
	return	new
if __name__ == "__main__":
	a = raw_input()
	str = leftRotating(a, 2)
	print str