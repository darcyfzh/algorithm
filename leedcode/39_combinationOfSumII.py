'''
@Author: Darcy
@Date: May, 26, 2017
@Topic:
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is:[[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]
'''
def combinationSum2(candidates, target):
        result = []
        candidates.sort()
        def dfs(remain, begin, stack, candidates):
            if remain == 0: 
                result.append(stack)
                return
            for i in xrange(beg, len(candidates)):
                if candidates[i] > remain: 
                	break
                dfs(remain - candidates[i], i+1, stack + [candidates[i]], candidates) 
        dfs(target, 0, [], candidates)
        result = [sorted(item) for item in result]
        result = list(set([tuple(item) for item in result]))
        result = [list(item) for item in result]
        return result

print combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

