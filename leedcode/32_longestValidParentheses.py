def longestValidParentheses(s):
	dp,stack = [0] * (len(s) + 1),[]
	for i in range(len(s)):
		if s[i] == '(':
			stack.append(i)
		else:
			if stack:
                p = stack.pop()
			    d[i + 1] = dp[p] + i - p + 1
s = input()
result = longestValidParentheses(s)
print (result)