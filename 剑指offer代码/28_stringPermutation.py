# # def permutation(str):
# # 	if str == None:
# # 		return
# # 	support(str, 0)

# def support(str, a):
# 	size = len(str)
# 	if a == size:
# 		#result.append(str)
# 		print str
# 	else:
# 		for i in range(a, size):
# 			temp = str[i]
# 			str[i] = str[a]
# 			str[a] = temp
# 			support(str, a + 1)
# 			temp = str[i]
# 			str[i] = str[a]
# 			str[a] = temp

# if __name__ == "__main__":
# 	result = []
# 	#permutation([1,2,3])
# 	support([1,2,4], 0)
# 	print result
import itertools
result = list(itertools.permutations([0,1,2,3,4,5,6,7],8))
count = 0
for index, arr in enumerate(result):
	for i in range(7):
		for j in range(i + 1, 8):
			if i - j == arr[i] - arr[j]:
				count += 1
print count

