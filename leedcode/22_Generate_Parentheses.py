def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens.append(p)
        return parens
def generateParenthesis(n):
    return generate('', n, n)

print (generateParenthesis(3))