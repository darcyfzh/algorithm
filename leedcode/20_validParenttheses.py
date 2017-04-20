def validParenttheses(s):
	dict = {"]":"[", "}":"{", ")":"("}
	stack = []
	for i in range(len(s)):
		if s[i] in dic.values():
			stack.append(s[i])
		elif s[i] in dic.keys():
			if stack == [] or dic[s[i]] != stack.pop():
				return False
		else:
			return False
	return stack == []
