# 给定一个非负整数数组a1，a2，a3，...，an，每个元素代表一个坐标（1，a1），...，（i，ai），...，（n，an）。从（i，0）到（i，ai）画条直线。找出两条直线，使得这两条直线和x轴形成的容器可以装最多的水。
# 思路：
# 其实，本问题就是要求找到两个下标i和j，使(i-j)*min(ai,aj)最大。我们注意到，如果ai<aj，i<j，那么对于任意i<k<j，(i-k)*min(ai,ak)<(i-j)*min(ai,aj)。所以，当果ai<aj，i<j时，要i++；同理，当果ai>aj，i<j时，要j--。
# 算法从i=1, j=n开始扫描，最后当i=j时就可以找到最大的装水容器。复杂度是O(n)。
def container(a):
	if len(a) <= 1:
		return 0
	i = 0
	j = len(a) - 1
	best = (j - i) * min(a[i], a[j])
    while(i < j):
    	area = (j - i) * min(a[i], a[j])
    	if area < best:
    		best = area
    	if a[i] < a[j]:
    		i++
    	else:
    		j--
    return best

if __name__ == "__main__":
	a = [int(x) for x in input().strip().split()]
	best = container(a)
	print best